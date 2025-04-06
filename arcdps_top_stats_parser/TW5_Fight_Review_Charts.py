from dataclasses import dataclass,field
import os.path
from os import listdir
from enum import Enum
from xlutils.copy import copy
import json
import datetime
import gzip
import math

from collections import OrderedDict

#Change input_directory to match json log location
input_directory = 'D:\\GW2Logs\\Output\\'

files = listdir(input_directory)
sorted_files = sorted(files)

fileDate = datetime.datetime.now()
#fileTid = fileDate.strftime('%Y%m%d%H%M')+"_Fight_Review.tid"
#output = open(fileTid, "w",encoding="utf-8")

def myprint(output_file, output_string):
    print(output_string)
    output_file.write(output_string+"\n")

def buildStatData(player, fightSeconds, stat):

    playerData = {}
    playerDataOutput = []

    for statChange in player[stat]:
        statTime = int(statChange[0]/1000)
        statPct = statChange[1]
    # if hpTime not in playerData:
    # playerData[hpTime] = 0
        playerData[statTime] = statPct

    cur_statPct = 100

    for phase in range(0, fightSeconds+1):
        if phase in playerData:
            cur_statPct = playerData[phase]
            playerDataOutput.append(str(cur_statPct))
        else:
            playerDataOutput.append(str(cur_statPct))

    return playerDataOutput

    
FightReview = {}
for filename in sorted_files:
    # skip files of incorrect filetype
    file_start, file_extension = os.path.splitext(filename)
    #if args.filetype not in file_extension or "top_stats" in file_start:
    if file_extension not in ['.json', '.gz'] or "top_stats" in file_start:
        continue

    print_string = "parsing "+filename
    print(print_string)
    file_path = "".join((input_directory,"/",filename))

    if file_extension == '.gz':
        with gzip.open(file_path, mode="r") as f:
            json_data = json.loads(f.read().decode('utf-8'))
    else:
        json_datafile = open(file_path, encoding='utf-8')
        json_data = json.load(json_datafile)    
    

    if 'usedExtensions' not in json_data:
        players_running_healing_addon = []
    else:
        extensions = json_data['usedExtensions']
        for extension in extensions:
            if extension['name'] == "Healing Stats":
                players_running_healing_addon = extension['runningExtension']    

                
    FightReview[filename]={}
    FightReview[filename]['EnemyDamage'] = {}
    FightReview[filename]['SquadDamage'] = {}
    FightReview[filename]['SquadSkills'] = {}
    FightReview[filename]['SquadDeaths'] = {}
    FightReview[filename]['EnemyDeaths'] = {}
    FightReview[filename]['TagHpPct'] = {}
    FightReview[filename]['TagBaPct'] = {}
    FightReview[filename]['SquadHpPct'] = {}
    FightReview[filename]['SquadBaPct'] = {}    
    players = json_data['players']
    targets = json_data['targets']
    skillMap = json_data['skillMap']
    buffMap = json_data['buffMap']
    if 'mechanicss' in json_data:
        mechanics = json_data['mechanicss']
    else:
        continue

    
    FightReview[filename]['EnemyCount'] = len(targets)
    FightReview[filename]['SquadCount'] = len(players)
    
    for player in players:
        if player['hasCommanderTag']:
            FightReview[filename]['Tag'] = player['name']
            if 'healthPercents' in player:
                for hpChange in player['healthPercents']:
                    hpTime = int(hpChange[0]/1000)
                    hpPct = hpChange[1]
                    if hpTime not in FightReview[filename]['TagHpPct']:
                        FightReview[filename]['TagHpPct'][hpTime] = 0
                    FightReview[filename]['TagHpPct'][hpTime] = hpPct
            if 'barrierPercents' in player:
                for baChange in player['barrierPercents']:
                    baTime = int(baChange[0]/1000)
                    baPct = baChange[1]
                    if baTime not in FightReview[filename]['TagBaPct']:
                        FightReview[filename]['TagBaPct'][baTime] = 0
                    FightReview[filename]['TagBaPct'][baTime] = baPct
            break
        else:
            FightReview[filename]['Tag'] = "Tag not Found"
            
    for player in players:
        if 'targetDamage1S' in player:
            for cur_target in player['targetDamage1S']:
                for phase, value in enumerate(cur_target[0]):
                    if phase not in FightReview[filename]['SquadDamage']:
                        FightReview[filename]['SquadDamage'][phase]=0
                    FightReview[filename]['SquadDamage'][phase] += value
                    if phase not in FightReview[filename]['SquadDeaths']:
                        FightReview[filename]['SquadDeaths'][phase]=0
                    #EnemyDeaths
                    if phase not in FightReview[filename]['EnemyDeaths']:
                        FightReview[filename]['EnemyDeaths'][phase]=0
                    
        if 'healthPercents' in player:
            for hpChange in player['healthPercents']:
                hpTime = int(hpChange[0]/1000)
                hpPct = hpChange[1]
                if player['name'] not in FightReview[filename]['SquadHpPct']:
                    FightReview[filename]['SquadHpPct'][player['name']]={}
                if hpTime not in FightReview[filename]['SquadHpPct'][player['name']]:
                    FightReview[filename]['SquadHpPct'][player['name']][hpTime] = 0
                FightReview[filename]['SquadHpPct'][player['name']][hpTime] = hpPct

                    
        if 'rotation' in player:
            for item in player['rotation']:
                for skillUsage in item['skills']:
                    castTime = int(skillUsage['castTime']/1000)
                    if castTime not in FightReview[filename]['SquadSkills']:
                        FightReview[filename]['SquadSkills'][castTime] = 0
                    FightReview[filename]['SquadSkills'][castTime] += 1
                    
                
    for target in targets:
        if 'damage1S' in target:
            for phase, value in enumerate(target['damage1S'][0]):
                if phase not in FightReview[filename]['EnemyDamage']:
                    FightReview[filename]['EnemyDamage'][phase]=0
                FightReview[filename]['EnemyDamage'][phase] += value
                                
    for mechanic in mechanics:
        if 'Dead' in mechanic['name']:
            for death in mechanic['mechanicsData']:
                deathTime = int(death['time']/1000)
                if deathTime not in FightReview[filename]['SquadDeaths']:
                    FightReview[filename]['SquadDeaths'][deathTime]=0
                FightReview[filename]['SquadDeaths'][deathTime]+=1
        
        if "Kllng.Blw.Player" in mechanic['name']:
            for death in mechanic['mechanicsData']:
                deathTime = int(death['time']/1000)
                if deathTime not in FightReview[filename]['EnemyDeaths']:
                    FightReview[filename]['EnemyDeaths'][deathTime]=0
                FightReview[filename]['EnemyDeaths'][deathTime]+=1

print("Complete")