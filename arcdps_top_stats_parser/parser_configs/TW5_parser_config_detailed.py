#    This file contains the configuration for computing the detailed top stats in arcdps logs as parsed by Elite Insights.
#    Copyright (C) 2021 Freya Fleckenstein
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

stats_to_compute = ['deaths', 'downed', 'iol', 'res', 'kills', 'downs','dmg', 'Pdmg', 'Cdmg', 'shieldDmg', 'dmgAll','dmg_taken', 'rips', 'cleanses', 'superspeed', 'stealth', 'HiS', 'dist', 'stability', 'protection', 'aegis', 'might', 'fury', 'resistance', 'resolution', 'quickness', 'swiftness', 'alacrity', 'vigor', 'regeneration', 'heal', 'barrier', 'barrierDamage', 'swaps', 'dodges', 'evades', 'invulns', 'hitsMissed', 'interupted', 'blocks', 'fireOut', 'shockingOut', 'frostOut', 'magneticOut', 'lightOut', 'darkOut', 'chaosOut', 'ripsIn', 'cleansesIn', 'resOutTime', 'cleansesOutTime', 'ripsOutTime', 'downContribution', 'againstDownedDamage', 'againstDownedCount', 'receivedCrowdControl', 'receivedCrowdControlDuration', 'appliedCrowdControl', 'appliedCrowdControlDuration', 'stunBreak', 'removedStunDuration']
aurasIn_to_compute = ['fireIn', 'shockingIn', 'frostIn', 'magneticIn', 'lightIn', 'darkIn', 'chaosIn']
aurasOut_to_compute = ['fireOut', 'shockingOut', 'frostOut', 'magneticOut', 'lightOut', 'darkOut', 'chaosOut']
defenses_to_compute = ['dmg_taken', 'barrierDamage', 'hitsMissed', 'interupted', 'invulns', 'evades', 'blocks', 'dodges', 'cleansesIn', 'ripsIn', 'downed', 'deaths', 'receivedCrowdControl', 'receivedCrowdControlDuration']
#defense_to_compute =['dmg_taken','blockedCount', 'evadedCount', 'missedCount', 'dodgeCount', 'invulnedCount', 'damageBarrier', 'interruptedCount', 'downCount', 'deadCount']


# Settings for output tiddler
summary_title = "WVW Log Review"
summary_creator = "Drevarr"

# How many players will be listed who achieved top stats most often for each stat?
num_players_listed = 50
# What portion (%) of are considered to be "top" in each fight for each stat?
num_players_considered_top_percentage = 5

# For the initial sorting of tables: 'total' or 'average'
player_sorting_stat_type = 'total'

# For what portion of all fights does a player need to be there to be considered for "consistency percentage" awards?
attendance_percentage_for_percentage = 50
# For what portion of all fights does a player need to be there to be considered for "late but great" awards?
attendance_percentage_for_late = 50
# For what portion of all fights does a player need to be there to be considered for "jack of all trades" awards? 
attendance_percentage_for_buildswap = 30
# For what portion of all fights does a player need to be there to be considered for "top average" awards? 
attendance_percentage_for_average = 33
# For what portion of all fights does a player need to be there to be considered at all
attendance_percentage_for_top = 1

# What portion of the top total player stat does someone need to reach to be considered for total awards?
percentage_of_top_for_consistent = 5
# What portion of the total stat of the top consistent player does someone need to reach to be considered for consistency awards?
percentage_of_top_for_total = 5
# What portion of the total stat of the top consistent player does someone need to reach to be considered for consistency awards?
percentage_of_topDamage_for_total = 0
# What portion of the total stat of the top consistent player does someone need to reach to be considered for consistency awards?
percentage_of_top_for_average = 5
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for percentage awards?
percentage_of_top_for_percentage = 5
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for late but great awards?
percentage_of_top_for_late = 75
# What portion of the percentage the top consistent player reached top does someone need to reach to be considered for jack of all trades awards?
percentage_of_top_for_buildswap = 75

# minimum number of allied players to consider a fight in the stats
min_allied_players = 5
# minimum duration of a fight to be considered in the stats
min_fight_duration = 15
# minimum number of enemies to consider a fight in the stats
min_enemy_players = 5

# Produce Charts for stats_to_compute
charts = True
# Include the Squad Comp and Fight Review tabs
include_comp_and_review = True

# Check for unknown team IDs in current fights
check_for_unknown_team_ids = True

# if overview_only = True, do not build individual tables & charts for stats in overview table,currently for Offensive and Defensive tabs 
damage_overview_only = False
defensive_overview_only = False

ignore_role_in_skill_cast = False

# Use PlenBot Logs? Set to True
# Requires the "save logs to a CSV file" option to be checked in PlenBot
use_PlenBot = False
# Plenbot Install Directory, change to match your installation
PlenBotPath = "d:\\PlenBot\\"


# names as which each specialization will show up in the stats
profession_abbreviations = {}
profession_abbreviations["Guardian"] = "Guardian"
profession_abbreviations["Dragonhunter"] = "Dragonhunter"
profession_abbreviations["Firebrand"] = "Firebrand"
profession_abbreviations["Willbender"] = "Willbender"

profession_abbreviations["Revenant"] = "Revenant"
profession_abbreviations["Herald"] = "Herald"
profession_abbreviations["Renegade"] = "Renegade"
profession_abbreviations["Vindicator"] = "Vindicator"    

profession_abbreviations["Warrior"] = "Warrior"
profession_abbreviations["Berserker"] = "Berserker"
profession_abbreviations["Spellbreaker"] = "Spellbreaker"
profession_abbreviations["Bladesworn"] = "Bladesworn"

profession_abbreviations["Engineer"] = "Engineer"
profession_abbreviations["Scrapper"] = "Scrapper"
profession_abbreviations["Holosmith"] = "Holosmith"
profession_abbreviations["Mechanist"] = "Mechanist"    

profession_abbreviations["Ranger"] = "Ranger"
profession_abbreviations["Druid"] = "Druid"
profession_abbreviations["Soulbeast"] = "Soulbeast"
profession_abbreviations["Untamed"] = "Untamed"    

profession_abbreviations["Thief"] = "Thief"
profession_abbreviations["Daredevil"] = "Daredevil"
profession_abbreviations["Deadeye"] = "Deadeye"
profession_abbreviations["Specter"] = "Specter"

profession_abbreviations["Elementalist"] = "Elementalist"
profession_abbreviations["Tempest"] = "Tempest"
profession_abbreviations["Weaver"] = "Weaver"
profession_abbreviations["Catalyst"] = "Catalyst"

profession_abbreviations["Mesmer"] = "Mesmer"
profession_abbreviations["Chronomancer"] = "Chronomancer"
profession_abbreviations["Mirage"] = "Mirage"
profession_abbreviations["Virtuoso"] = "Virtuoso"
    
profession_abbreviations["Necromancer"] = "Necromancer"
profession_abbreviations["Reaper"] = "Reaper"
profession_abbreviations["Scourge"] = "Scourge"
profession_abbreviations["Harbinger"] = "Harbinger"

# name each stat will be written as
stat_names = {}
stat_names["dmg"] = "Damage"
stat_names["Pdmg"] = "Power Damage"
stat_names["Cdmg"] = "Condi Damage"
stat_names["shieldDmg"] = "Shield Damage"
stat_names["dmgAll"] = "Damage All"
stat_names["dmg_taken"] = "Damage Taken"
stat_names["rips"] = "Boon Strips"
stat_names["stability"] = "Stability"
stat_names["protection"] = "Protection"
stat_names["aegis"] = "Aegis"
stat_names["might"] = "Might"
stat_names["fury"] = "Fury"
stat_names["cleanses"] = "Condition Cleanses"
stat_names["heal"] = "Healing"
stat_names["barrier"] = "Barrier"
stat_names["barrierDamage"] = "Barrier Damage"
stat_names["dist"] = "Distance to Tag"
stat_names["deaths"] = "Deaths"
stat_names["downed"] = "Downed"
stat_names["superspeed"] = "Superspeed"
stat_names["stealth"] = "Stealth"
stat_names["HiS"] = "Hide in Shadows"
stat_names["regeneration"] = "Regeneration"
stat_names["resistance"] = "Resistance"
stat_names["resolution"] = "Resolution"
stat_names["quickness"] = "Quickness"
stat_names["swiftness"] = "Swiftness"
stat_names["alacrity"] = "Alacrity"
stat_names["vigor"] = "Vigor"
stat_names["res"] = "Resurrect"
stat_names["iol"] = "Illusion of Life"
stat_names["cripple"] = "Cripple"
stat_names["weakness"] = "Weakness"
stat_names["daze"] = "Daze"
stat_names["immobilize"] = "Immobilize"
stat_names["swaps"] = "Weapon Swaps"
stat_names["kills"] = "Enemies Killed"
stat_names["downs"] = "Enemies Downed"
stat_names["dodges"] = "Dodge Attempts"
stat_names["evades"] = "Evaded Attacks"
stat_names["blocks"] = "Blocked Attacks"
stat_names["invulns"] = "Invulnerable to Attacks"
stat_names["interupted"] = "Interupted"
stat_names["hitsMissed"] = "Hits Missed Against"
stat_names["fireOut"] = "Fire Aura"
stat_names["shockingOut"] = "Shocking Aura"
stat_names["frostOut"] = "Frost Aura"
stat_names["magneticOut"] = "Magnetic Aura"
stat_names["lightOut"] = "Light Aura"
stat_names["darkOut"] = "Dark Aura"
stat_names["chaosOut"] = "Chaos Aura"
stat_names["ripsIn"] = "Boon Strips Incoming"
stat_names["ripsTime"] = "Boon Time Lost"
stat_names["cleansesIn"] = "Condition Cleanses Incoming"
stat_names["cleansesTime"] = "Condition Time Cleared"
stat_names["downContrib"] = "Down Contribution in Damage"
stat_names["resOutTime"] = "Time Spent Ressurecting"
stat_names["cleansesOutTime"] = "Duration of Conditions Cleansed"
stat_names["ripsOutTime"] = "Duration of Boons Stripped"
stat_names["downContribution"] = "Down Contribution"
stat_names["againstDownedCount"] = "Against Downed Count"
stat_names["againstDownedDamage"] = "Against Downed Damage"
stat_names['receivedCrowdControl'] = "Received Hard CC"
stat_names['receivedCrowdControlDuration'] = "Received Hard CC Duration"
stat_names['appliedCrowdControl'] = "Applied Hard CC"
stat_names['appliedCrowdControlDuration'] = "Applied Hard CC Duration"
stat_names['stunBreak'] = "Stun Breaks"
stat_names['removedStunDuration'] = "Stun Duration Removed"

buffs_defensive = {
    17047: "Virtue of Resolve (Battle Presence - Absolute Resolve)", 19083: "Oil Mastery III (Increased Armor)", 21484: "Iron Hide (Ram)",
    21780: "Skelk Venom", 24304: "Stone Heart", 26596: "Rite of the Great Dwarf", 27737: "Infuse Light", 29379: "Naturalistic Resonance",
    29726: "Last Rites", 29906: "Shield of Courage (Active)", 30285: "Vampiric Aura", 31229: "Watchful Eye", 31337: "Rebound",
    33330: "Rite of the Great Dwarf (Ancient Echo)", 33978: "Healing Mist", 34281: "Guard!", 40045: "Bear Stance", 41815: "Dolyak Stance",
    42249: "Photon Barrier Buff", 42925: "Eternal Oasis", 43194: "Unbroken Lines", 43401: "Unflinching Fortitude", 43487: "Signet of Courage (Shared)",
    44682: "Breakrazor's Bastion", 45910: "Defy Pain", 46554: "Signet of Resolve (Shared)", 50415: "Stone Spirit", 51677: "Facet of Nature-Dwarf",
    51699: "Facet of Nature-Centaur", 55026: "Glyph of the Stars (CA)", 55048: "Glyph of the Stars",
}

buffs_offensive = {
    36781: "Unblockable", 31487: "Static Charge", 38333: "Pinpoint Distribution", 41957: "Ashes of the Just", 9240: "Bane Signet (PI)",
    9237: "Signet of Wrath (PI)", 31803: "Glyph of Empowerment", 50421: "Frost Spirit", 50413: "Sun Spirit", 14055: "Spotter",
    44651: "Vulture Stance", 44139: "One Wolf Pack", 51692: "Facet of Nature-Assassin", 41016: "Razorclaw's Rage",
    45026: "Soulcleave's Summit", 26854: "Assassin's Presence", 63168: "Rot Wallow Venom", 13054: "Skale Venom", 13036: "Spider Venom",
    49083: "Soul Stone Venom", 14417: "Banner of Strength", 14449: "Banner of Discipline", 14222: "Empower Allies",
}

buffs_support = {
    890: "Revealed", 5577: "Shocking Aura", 5579: "Frost Aura", 5677: "Fire Aura", 5684: "Magnetic Aura", 5974: "Superspeed",
    9231: "Merciful Intervention (Target)", 9235: "Merciful Intervention (Self)", 10269: "Hide in Shadows", 10332: "Chaos Aura",
    10346: "Illusion of Life", 13017: "Stealth", 13094: "Devourer Venom", 13095: "Ice Drake Venom", 13133: "Basilisk Venom",
    14450: "Banner of Tactics", 15788: "Conjure Earth Shield", 15789: "Conjure Flame Axe", 15790: "Conjure Frost Bow",
    15791: "Conjure Lightning Hammer", 15792: "Conjure Fiery Greatsword", 25518: "Light Aura", 30462: "Heat Sync",
    34236: "Search and Rescue!", 39978: "Dark Aura", 45038: "Moa Stance", 46280: "Griffon Stance", 50381: "Storm Spirit",
    51674: "Facet of Nature-Dragon", 51704: "Facet of Nature-Demon", 63093: "Shrouded"
}