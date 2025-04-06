#!/usr/bin/env python3

from os import listdir
import argparse
import os.path
import sys
import importlib
import json
import datetime
import gzip
import xlsxwriter

from TW5_parse_top_stats_tools import fill_config, reset_globals, get_stats_from_fight_json, get_stat_from_player_json, get_buff_ids_from_json, get_combat_time_breakpoints, sum_breakpoints, BuffGenerationType

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='This reads a set of arcdps reports in xml format and generates top stats.')
	parser.add_argument('input_directory', help='Directory containing .xml or .json files from arcdps reports')
	parser.add_argument('-c', '--config_file', dest="config_file", help="Config file with all the settings", default="TW5_parser_config_detailed")
	parser.add_argument('-a', '--anonymized', dest="anonymize", help="Create an anonymized version of the top stats. All account and character names will be replaced.", default=False, action='store_true')
	args = parser.parse_args()

	if not os.path.isdir(args.input_directory):
		print("Directory ",args.input_directory," is not a directory or does not exist!")
		sys.exit()

	log = open(args.input_directory+"/log_detailed.txt", "w")

	parser_config = importlib.import_module("parser_configs."+args.config_file , package=None) 
	config = fill_config(parser_config)
	
	# create xls file if it doesn't exist
	#book = xlwt.Workbook(encoding="utf-8")
	book = xlsxwriter.Workbook(args.input_directory+"/TW5_top_stats_per_fight.xlsx")
	#sheet1 = book.add_sheet("Player Stats")
	sheet1 = book.add_worksheet("Player Stats")

	headers = []

	headers.append("Account")
	headers.append("Name")
	headers.append("Profession")
	headers.append("Role")
	headers.append("Rally Num")
	headers.append("Fight Num")
	headers.append("Date")
	headers.append("Start Time")
	headers.append("End Time")
	headers.append("Num Allies")
	headers.append("Num Party Members")
	headers.append("Num Enemies")
	headers.append("Group")
	headers.append("Duration")
	headers.append("Combat time")
	headers.append("Target Damage")
	headers.append("Target Power Damage")
	headers.append("Target Condi Damage")
	headers.append("All Damage")
	headers.append("All Power Damage")
	headers.append("All Condi Damage")
	headers.append("Crit Perc")
	headers.append("Flanking Perc")
	headers.append("Glancing Perc")
	headers.append("Blind Num")
	headers.append("Interrupt Num")
	headers.append("Invulnerable Num")
	headers.append("Evaded Num")
	headers.append("Blocked Num")

	stats_to_compute = ['downs', 'kills', 'res', 'deaths', 'dmg_taken', 'barrierDamage', 'dist',  'swaps', 'rips', 'cleanses', 'barrier']
	for i,stat in enumerate(stats_to_compute):
		headers.append(config.stat_names[stat])
	
	headers.append('Total Healing')
	headers.append('Power Healing')
	headers.append('Conversion Healing')
	headers.append('Hybrid Healing')
	headers.append('Group Total Healing')
	headers.append('Group Power Healing')
	headers.append('Group Conversion Healing')
	headers.append('Group Hybrid Healing')

	uptime_Order = ['protection',  'aegis',  'fury',  'resistance',  'resolution',  'quickness',  'swiftness',  'alacrity',  'vigor',  'regeneration']
	stacking_uptime_Order =  ['stability',  'might']

	for i,stat in enumerate(uptime_Order + stacking_uptime_Order):
		headers.append(stat.capitalize()+" Squad Gen")

	for i,stat in enumerate(uptime_Order + stacking_uptime_Order):
		headers.append(stat.capitalize()+" Group Gen")

	for i,stat in enumerate(uptime_Order + stacking_uptime_Order):
		headers.append(stat.capitalize()+" Self Gen")

	for i,stat in enumerate(uptime_Order):
		headers.append(stat.capitalize()+" Uptime")

	headers.append("Stab Avg Stacks")
	headers.append("Stab 1+ Stacks")
	headers.append("Stab 2+ Stacks")
	headers.append("Stab 5+ Stacks")

	headers.append("Might Avg Stacks")
	headers.append("Might 10+ Stacks")
	headers.append("Might 15+ Stacks")
	headers.append("Might 20+ Stacks")
	headers.append("Might 25 Stacks")

	for i,stat in enumerate(uptime_Order + ['stability']):
		headers.append(stat.capitalize()+" Uptime while damaging")

	headers.append("Might Avg Stack while damaging")
	headers.append("Might 10+ Stacks while damaging")
	headers.append("Might 15+ Stacks while damaging")
	headers.append("Might 20+ Stacks while damaging")
	headers.append("Might 25 Stacks while damaging")

	headers.append("Carrion Damage")
	for i in range(1, 21):
		headers.append('Chunk Damage (' + str(i) + ')')
	for i in range(1, 21):
		headers.append('Burst Damage (' + str(i) + ')')
	for i in range(1, 21):
		headers.append('Ch5Ca Burst Damage (' + str(i) + ')')

	Control_Effects = {720: 'Blinded', 721: 'Crippled', 722: 'Chilled', 727: 'Immobile', 742: 'Weakness', 791: 'Fear', 833: 'Daze', 872: 'Stun', 26766: 'Slow', 27705: 'Taunt', 30778: "Hunter's Mark", 738:'Vulnerability'}
	for conditionId in Control_Effects:
		headers.append(Control_Effects[conditionId] + ' Gen')
	
	Auras_Order = {5677: 'Fire', 5577: 'Shocking', 5579: 'Frost', 5684: 'Magnetic', 25518: 'Light', 39978: 'Dark', 10332: 'Chaos'}
	for auraId in Auras_Order:
		headers.append(Auras_Order[auraId] + ' Aura Out')
	for auraId in Auras_Order:
		headers.append(Auras_Order[auraId] + ' Aura In')

	#Set formatting for header
	header_format = book.add_format()
	header_format.set_bold()
	header_format.set_text_wrap()
	header_format.set_align('center')
	header_format.set_align('bottom')
	header_format.set_font_color('navy') # Go Navy! Beat Army.
	#Set Top Row frozen
	sheet1.freeze_panes(1, 0)


	for i, header in enumerate(headers):
		sheet1.write(0, i, header, header_format)

	# iterating over all fights in directory
	files = listdir(args.input_directory)
	sorted_files = sorted(files)
	rally_num = 1
	fight_num = 1
	last_fight_end_time = None
	row = 1
	for filename in sorted_files:
		file_start, file_extension = os.path.splitext(filename)
		if file_extension not in ['.json', '.gz'] or "top_stats" in file_start:
			continue

		print("parsing "+filename)
		file_path = "".join((args.input_directory,"/",filename))

		if file_extension == '.gz':
			with gzip.open(file_path, mode="r") as f:
				json_data = json.loads(f.read().decode('utf-8'))
		else:
			json_datafile = open(file_path, encoding='utf-8')
			json_data = json.load(json_datafile)

		reset_globals()
		config = fill_config(parser_config)
		get_buff_ids_from_json(json_data, config)
		fight, players_running_healing_addon, squad_offensive, squad_Control, enemy_Control, enemy_Control_Player, downed_Healing, uptime_Table, stacking_uptime_Table, auras_TableIn, auras_TableOut, Death_OnTag, Attendance, DPS_List, CPS_List, SPS_List, HPS_List, DPSStats = get_stats_from_fight_json(json_data, config, log)
		
		if fight.skipped:
			continue


		if last_fight_end_time:
			after_last_fight = datetime.datetime.fromisoformat(last_fight_end_time) + datetime.timedelta(hours=2)
			if after_last_fight <  datetime.datetime.fromisoformat(fight.start_time):
				print("Start of a new rally at ", fight.start_time)
				rally_num += 1
				fight_num = 1

		last_fight_end_time = fight.end_time

		party_member_counts = {}
		for player_data in json_data['players']:
			group = player_data['group']
			if group in party_member_counts:
				party_member_counts[group] += 1
			else:
				party_member_counts[group] = 1

		for squadDps_prof_name in DPSStats:
			player = [p for p in json_data["players"] if p['account'] == DPSStats[squadDps_prof_name]['account']][0]
			player_name = player['name']
			player_prof_name = "{{"+player['profession']+"}} "+player_name
			player_prof_name_alt = player_name + "_{{"+player['profession']+"}}"

			fight_duration = json_data["durationMS"] / 1000
			combat_time = sum_breakpoints(get_combat_time_breakpoints(player)) / 1000
			num_party_members = party_member_counts[player['group']]

			# Calculate healing values
			if player_name in players_running_healing_addon and 'extHealingStats' in player:
				total_healing = 0
				total_healing_group = 0
				power_healing = 0
				power_healing_group = 0
				conversion_healing = 0
				conversion_healing_group = 0
				hybrid_healing = 0
				hybrid_healing_group = 0

				allied_healing_1s = player['extHealingStats']['alliedHealing1S']
				allied_power_healing_1s = player['extHealingStats']['alliedHealingPowerHealing1S']
				allied_conversion_healing_1s = player['extHealingStats']['alliedConversionHealingHealing1S']
				allied_hybrid_healing_1s = player['extHealingStats']['alliedHybridHealing1S']
				for index in range(len(json_data['players'])):
					is_same_group = player['group'] == json_data['players'][index]['group']

					player_healing = allied_healing_1s[index][0][-1]
					player_power_healing = allied_power_healing_1s[index][0][-1]
					player_conversion_healing = allied_conversion_healing_1s[index][0][-1]
					player_hybrid_healing = allied_hybrid_healing_1s[index][0][-1]


					total_healing += player_healing
					power_healing += player_power_healing
					conversion_healing += player_conversion_healing
					hybrid_healing += player_hybrid_healing
					if is_same_group:
						total_healing_group += player_healing
						power_healing_group += player_power_healing
						conversion_healing_group += player_conversion_healing
						hybrid_healing_group += player_hybrid_healing
			else:
				# When no healing stats data, set to -1
				total_healing = -1
				total_healing_group = -1
				power_healing = -1
				power_healing_group = -1
				conversion_healing = -1
				conversion_healing_group = -1
				hybrid_healing = -1
				hybrid_healing_group = -1

			row_data = []

			row_data.append(DPSStats[squadDps_prof_name]['account'])
			row_data.append(DPSStats[squadDps_prof_name]['name'])
			row_data.append(DPSStats[squadDps_prof_name]['profession'])
			row_data.append(DPSStats[squadDps_prof_name]['role'])
			row_data.append(rally_num)
			row_data.append(fight_num)
			row_data.append(fight.start_time.split()[0])
			row_data.append(fight.start_time.split()[1])
			row_data.append(fight.end_time.split()[1])
			row_data.append(fight.allies)
			row_data.append(num_party_members)
			row_data.append(fight.enemies)
			row_data.append(int(player['group']))
			row_data.append(fight_duration)
			row_data.append(combat_time)
			row_data.append(get_stat_from_player_json(player, players_running_healing_addon, 'dmg', config))
			row_data.append(get_stat_from_player_json(player, players_running_healing_addon, 'Pdmg', config))
			row_data.append(get_stat_from_player_json(player, players_running_healing_addon, 'Cdmg', config))
			row_data.append(int(player['dpsAll'][0]['damage']) )
			row_data.append(int(player['dpsAll'][0]['powerDamage']) )
			row_data.append(int(player['dpsAll'][0]['condiDamage']) )

			if squad_offensive[player_prof_name]['stats']['critableDirectDamageCount'] > 0:
				row_data.append(squad_offensive[player_prof_name]['stats']['criticalRate'] / squad_offensive[player_prof_name]['stats']['critableDirectDamageCount'])
			else:
				row_data.append(0)

			if squad_offensive[player_prof_name]['stats']['connectedDirectDamageCount'] > 0:
				row_data.append(squad_offensive[player_prof_name]['stats']['flankingRate'] / squad_offensive[player_prof_name]['stats']['connectedDirectDamageCount'])
				row_data.append(squad_offensive[player_prof_name]['stats']['glanceRate'] / squad_offensive[player_prof_name]['stats']['connectedDirectDamageCount'])
			else:
				row_data.append(0)
				row_data.append(0)

			row_data.append(squad_offensive[player_prof_name]['stats']['missed'])
			row_data.append(squad_offensive[player_prof_name]['stats']['interrupts'])
			row_data.append(squad_offensive[player_prof_name]['stats']['invulned'])
			row_data.append(squad_offensive[player_prof_name]['stats']['evaded'])
			row_data.append(squad_offensive[player_prof_name]['stats']['blocked'])

			for i,stat in enumerate(stats_to_compute):
				row_data.append(get_stat_from_player_json(player, players_running_healing_addon, stat, config))
			
			row_data.append(total_healing)
			row_data.append(power_healing)
			row_data.append(conversion_healing)
			row_data.append(hybrid_healing)
			row_data.append(total_healing_group)
			row_data.append(power_healing_group)
			row_data.append(conversion_healing_group)
			row_data.append(hybrid_healing_group)

			for i,stat in enumerate(uptime_Order):
				row_data.append((get_stat_from_player_json(player, players_running_healing_addon, stat, config)/100)*fight_duration*(fight.allies - 1))
			for i,stat in enumerate(stacking_uptime_Order):
				row_data.append(get_stat_from_player_json(player, players_running_healing_addon, stat, config)*fight_duration*(fight.allies - 1))

			for i,stat in enumerate(uptime_Order):
				row_data.append((get_stat_from_player_json(player, players_running_healing_addon, stat, config, False, BuffGenerationType.GROUP)/100)*fight_duration*(num_party_members - 1))
			for i,stat in enumerate(stacking_uptime_Order):
				row_data.append(get_stat_from_player_json(player, players_running_healing_addon, stat, config, False, BuffGenerationType.GROUP)*fight_duration*(num_party_members - 1))

			for i,stat in enumerate(uptime_Order):
				row_data.append((get_stat_from_player_json(player, players_running_healing_addon, stat, config, False, BuffGenerationType.SELF)/100)*fight_duration)
			for i,stat in enumerate(stacking_uptime_Order):
				row_data.append(get_stat_from_player_json(player, players_running_healing_addon, stat, config, False, BuffGenerationType.SELF)*fight_duration)
		
			uptime_duration = uptime_Table[player_prof_name]['duration']
			for i,stat in enumerate(uptime_Order):
				if stat in uptime_Table[player_prof_name]:
					buff_Time = uptime_Table[player_prof_name][stat]
					row_data.append(buff_Time / uptime_duration)
				else:
					row_data.append(0.00)

			stability_stacks = stacking_uptime_Table[squadDps_prof_name]['stability']
			stability_stacks_fight_time = (stacking_uptime_Table[squadDps_prof_name]['duration_stability'] / 1000) or 1

			might_stacks = stacking_uptime_Table[squadDps_prof_name]['might']
			might_stacks_fight_time = (stacking_uptime_Table[squadDps_prof_name]['duration_might'] / 1000) or 1
			
			row_data.append(sum(stack_num * stability_stacks[stack_num] for stack_num in range(1, 26)) / (stability_stacks_fight_time * 1000))
			row_data.append((1.0 - (stability_stacks[0] / (stability_stacks_fight_time * 1000))))
			row_data.append(sum(stability_stacks[i] for i in range(2,26)) / (stability_stacks_fight_time * 1000))
			row_data.append(sum(stability_stacks[i] for i in range(5,26)) / (stability_stacks_fight_time * 1000))

			row_data.append(sum(stack_num * might_stacks[stack_num] for stack_num in range(1, 26)) / (might_stacks_fight_time * 1000))
			row_data.append(sum(might_stacks[i] for i in range(10,26)) / (might_stacks_fight_time * 1000))
			row_data.append(sum(might_stacks[i] for i in range(15,26)) / (might_stacks_fight_time * 1000))
			row_data.append(sum(might_stacks[i] for i in range(20,26)) / (might_stacks_fight_time * 1000))
			row_data.append(might_stacks[25] / (might_stacks_fight_time * 1000))

			total_damage = DPSStats[squadDps_prof_name]["Damage_Total"] or 1

			for i,stat in enumerate(uptime_Order + ['stability']):
				row_data.append(stacking_uptime_Table[squadDps_prof_name]['damage_with_'+stat][1] / total_damage)
			
			damage_with_might = stacking_uptime_Table[squadDps_prof_name]['damage_with_might']

			row_data.append(sum(stack_num * damage_with_might[stack_num] for stack_num in range(1, 26)) / total_damage)
			row_data.append(sum(damage_with_might[i] for i in range(10,26)) / total_damage)
			row_data.append(sum(damage_with_might[i] for i in range(15,26)) / total_damage)
			row_data.append(sum(damage_with_might[i] for i in range(20,26)) / total_damage)
			row_data.append(damage_with_might[25] / total_damage)			

			row_data.append(DPSStats[squadDps_prof_name]['Carrion_Damage'])

			for i in range(1, 21):
				row_data.append(DPSStats[squadDps_prof_name]['Chunk_Damage'][i])

			for i in range(1, 21):
				row_data.append(DPSStats[squadDps_prof_name]['Burst_Damage'][i])

			for i in range(1, 21):
				row_data.append(DPSStats[squadDps_prof_name]['Ch5Ca_Burst_Damage'][i])

			for conditionId in Control_Effects:
				key = Control_Effects[conditionId]
				condition_value = 0
				if key in squad_Control and player_prof_name_alt in squad_Control[key]:
					condition_value = squad_Control[key][player_prof_name_alt]

				row_data.append(condition_value)

			for auraId in Auras_Order:
				key = Auras_Order[auraId]
				aura_value = 0
				if key in auras_TableOut and player_name in auras_TableOut[key]:
					aura_value = auras_TableOut[key][player_name]

				row_data.append(aura_value)

			for auraId in Auras_Order:
				key = Auras_Order[auraId]
				aura_value = 0
				if key in auras_TableIn and player_name in auras_TableIn[key]:
					aura_value = auras_TableIn[key][player_name]

				row_data.append(aura_value)

			for i, cell_data in enumerate(row_data):
				sheet1.write(row, i, cell_data)

			row += 1
		
		fight_num += 1

	#book.save(args.input_directory+"/TW5_top_stats_per_fight.xls")
	book.close()