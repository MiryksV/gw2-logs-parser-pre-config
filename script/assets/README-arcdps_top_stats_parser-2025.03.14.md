![GitHub](https://img.shields.io/github/license/Drevarr/arcdps_top_stats_parser)


![Alt](https://repobeats.axiom.co/api/embed/d07727b06a0bcacb7692ccd3c30bd9cfdb2394f7.svg "Repobeats analytics image")

# TW5 Modifications #

```TW5_parse_top_stats_detailed.py``` and ```TW5_parse_top_stats_tools.py``` provide alternative output to support posting to a TW5 wiki with shiraz plugin.
Example available at (https://fear.wvwlogs.com/)

Edit ```Example_Guild_Data.py``` to update with your guild id and API token then rename as ```Guild_Data.py```
      
      
      Guild_ID = 'Input_Your_Guild_ID_Here'
      
      API_Key = 'Input_Your_API_Token_Here'
      

Follow the ``` Preparation ``` steps further down in this document then utilize the ```TW5 Top Stats Generation Steps ``` to generate the wiki for online hosting.

![Example Output](images/ExampleOutput.PNG)

# What is it all about? #

Did you ever wonder how well you did compared to your squad mates, not only in a single fight, but over the whole raid? Do you want to know who to ask for help with a specific class? Or do you want to hand out an award to a guildie who did the most damage in all raids over a whole week? This project provides a tool for generating top stats from a set of arcdps logs, allowing you to easily identify top performing players in different stats.

Currently supported stats are: 
- all damage
- boon rips
- cleanses
- stability output (generation squad)
- protection output (generation squad)
- aegis output (generation squad)
- might output (generation squad)
- fury output (generation squad)
- healing output
- barrier output
- average distance to tag
- damage taken
- deaths

Healing and barrier output can only be analyzed when contained in the logs, i.e., the [healing addon for arcdps](https://github.com/Krappa322/arcdps_healing_stats/releases) is installed. They will only be analyzed for players who also have the addon installed, since data may be incomplete for others.

Provided are two scripts: ```TW5_parse_top_stats_detailed.py``` and ```TW5_parse_top_stats_per_fight.py```. The first gives an overview of top players considering consistency and total values of all desired stats. The second provides an ```.xlsx``` output showing the performance of all players contributing to each desired stat on a per fight basis.

Note that currently, this tool is meant only for analyzing wwv fights.

# How does it work? #
## Preparation ##
To be able to generate the top stats, you need to install/download a few things.
1. Install python3 if you don't have it yet (https://www.python.org/downloads/).
2. Install xlrd, xlutils, xlwt and jsons it you don't have them yet: Open a terminal (on windows press windows key + r, type "cmd", enter), and type ```pip3 install xlrd xlutils xlwt jsons requests xlsxwriter```, enter.
3. Get the Elite Insights parser for arcdps logs (https://github.com/baaron4/GW2-Elite-Insights-Parser/releases). For parsing including barrier, you will need version 2.41 or higher. In the following, we assume the path to it is ```C:\Users\Example\Downloads\EliteInsights\```.
4. Download this repository if you don't have it yet. We here assume the path is ```C:\Users\Example\Downloads\arcdps_top_stats_parser\```.

There are three methods for generating the top stats.
## TW5 Top Stats Generation Steps ##
1. Generate .json files from your arcdps logs by using Elite Insights. Enable detailed wvw parsing and combat replay computation. You can also use the EI settings file stored in this repository under ```EI_config\EI_detailed_json_combat_replay.conf```, which will generate .json files with detailed wvw parsing and combat replay.
2. Put all .json files you want included in the top stats into one folder. We use the folder ```C:\Users\Example\Documents\json_folder``` as an example here. Note that different file types will be ignored, so no need to move your .evtc/.zevtc logs elsewhere if you have them in the same folder.
3. Open a terminal / windows command line (press Windows key + r, type "cmd", enter).
4. Navigate to where the script is located using "cd", in our case this means ```cd Downloads\arcdps_top_stats_parser```.
5. Type ```python TW5_parse_top_stats_detailed.py <folder>```, where \<folder> is the path to your folder with json files. In our example case, we run ```python parse_top_stats_detailed.py C:\Users\Example\Documents\json_folder```. 
6. Open ```/example_output/TW5_Top_Stat_Parse.html``` in your browser of choice
7. Drag and Drop the resulting file ```TW5_top_stats_detailed.tid``` along with the ```*_TW5_Chart.tid``` files located in the \<folder> with your json files onto the top of the web page. The various ```*_TW5_Chart.tid``` files contain the js logic to generate the echarts.
  
  ![Screenshot_1](images/Screenshot_1.png)

8. Click the Import button on the popup
  
  ![Screenshot_2](images/Screenshot_2.png)

9. Log file link will be added to the WVW Log Review
  
  ![Screenshot_3](images/Screenshot_3.png)
  
10. Click the ![Save Button](images/Screenshot_4.png) button upper left side, complete the save dialog.
  
11. Upload to hosting site of choice

## TW5 Customization ##
![TW5_Top_Stat_Parse.html](https://github.com/Drevarr/arcdps_top_stats_parser/example_output/TW5_Top_Stat_Parse.html) is a single page application wiki that you can host to share the output of TW5_parse_top_stats_detailed.py

  * Detailed info regarding the wiki is available at https://tiddlywiki.com
  * You can rename TW5_Top_Stat_Parse.html to meet your hosting needs.
  * Replace TW5_Top_Stat_Parse.html#index.png with an appropriate image
  
## Manual Top Stats Generation ##
1. Generate .json files from your arcdps logs by using Elite Insights. Enable detailed wvw parsing and combat replay computation. You can also use the EI settings file stored in this repository under ```EI_config\EI_detailed_json_combat_replay.conf```, which will generate .json files with detailed wvw parsing and combat replay.
2. Put all .json files you want included in the top stats into one folder. We use the folder ```C:\Users\Example\Documents\json_folder``` as an example here. Note that different file types will be ignored, so no need to move your .evtc/.zevtc logs elsewhere if you have them in the same folder.
3. Open a terminal / windows command line (press Windows key + r, type "cmd", enter).
4. Navigate to where the script is located using "cd", in our case this means ```cd Downloads\arcdps_top_stats_parser```.
5. Type ```python parse_top_stats_detailed.py <folder>```, where \<folder> is the path to your folder with json files. In our example case, we run ```python parse_top_stats_overview.py C:\Users\Example\Documents\json_folder```. 

## Automated Top Stats Generation ##
For a more automated version, you can use the batch script ```TW5_parsing_arc_top_stats.bat``` as follows:
1. Move all logs you want included in the stats in one folder. We will use ```C:\Users\Example\Documents\log_folder\``` as an example.
2. Open a windows command line (press Windows key + r, type "cmd", enter).
3. Type ```<repo_folder>\parsing_arc_top_stats.bat "<log_folder>" "<Elite Insights folder>" "<repo_folder>"```. The full call in our example would be ```C:\Users\Example\Downloads\arcdps_top_stats_parser\parsing_arc_top_stats.bat "C:\Users\Example\Documents\log_folder\" "C:\Users\Example\Downloads\EliteInsights\" "C:\Users\Example\Downloads\arcdps_top_stats_parser\"```. This parses all logs in the log folder using EI with suitable settings and runs both scripts for generating the overview and detailed stats.

## Output ##
The console output for the overview and the detailed version shows you for each desired stat consistency and total awards. There are two exceptions: The first is distance to tag, where in our guild we found that the percentage of fights in which a top place was achieved is a more suitable measure for a job well done. The second is damage taken, where I compute the average damage taken per second based on time in combat and the person with least average damage taken gets a top spot. The overview also includes "late but great" and "Jack of all trades" awards if applicable. The award types are explained in detail on the [wiki](https://github.com/Freyavf/arcdps_top_stats_parser/wiki/Award-Types). Here is a short summary:
Consistency awards are given for players with top scores in the most fights. Total awards are given for overall top stats. Late but great awards are given to players who weren't there for all fights, but who achieved great consistency in the time they were there. Jack of all trades awards are given to people who swapped build at least once and achieved great consistency on one of their builds. Players can only win a late but great award or a Jack of all trades award if they didn't get a top consistency or top total award in the same category. 

Output files containing the tops stats are also generated in the json folder. By default, a .tid file containing the console output is created as ```top_stats_detailed.tid```. For further processing, a .xls and a .json file with the same names are also created. Furthermore, a log file that contains information on which files were skipped and why is also created in the json folder as ```log_detailed.txt```. 

## Settings ##
For changing any of the default settings, check out the wiki pages on ![command line options](https://github.com/Freyavf/arcdps_top_stats_parser/wiki/Command-line-options) and ![configuration options](https://github.com/Freyavf/arcdps_top_stats_parser/wiki/Configuration-options).
