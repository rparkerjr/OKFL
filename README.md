# OKFL
My workflow for cleaning fantasy football player data from MyFantasyLeague for the OKFL
---
My primary goals for this project were:
1. work on parsing and cleaning data
2. become more proficient with how to subset dataframes
3. get comfortable with plotting using matplotlib/pyplot and seaborn
4. find some useful insights about my fantasy football league!

Im sure there are already dozens of other scripts or analyses in this space, but this is meant as a learning tool for me.

## Data Source
Our league, OKFL, is hosted on the MyFantasyLeague website (http://home.myfantasyleague.com/). For this project I decided to stick with player data obtainable from MFL. The data does not reveal actual player performance (rushing yards, touchdowns, etc.) but rather it shows player scores by week based upon the scoring rules we have set up. 

These files are what I downloaded from the MFL website. The initial cleanup using PrepMFL() works on these files.
- OKFL Top 500 Offense 2016.csv
- OKFL Top 500 Offense 2017.csv
- OKFL Top 500 Offense 2018.csv

## Questions to Answer
Aside from the coding goals I listed above, I did want to answer a few specific questions about the data:
1. Are certain NFL teams better sources of players? IE, do certain teams regularly have high-scoring players while others are dogs?
2. How do the individual positions stack up against each other when it comes to player scores? 
<i>So it turns out that there are some interesting differences in the positions, at least based on our scoring system. QBs score the most week to week and have higher highs than the other positions. RBs are right behind them, with a few key players standing above the rest. But the bulk of the RB field is on par with WRs. TEs and PKs are similar when it comes to points scored, but PKs are more reliable and have a higher median; TEs skew lower.</i>
3. Are there discernible tiers of players? Does it make sense to focus on players within a tier vs. specific players?

## Update Log
### 7.15.19 : Added GetPlayers function
I found the help page for the MFL API and started tinkering with it. The first function I built was to get a listing of players with their player IDs. Next will be pulling the similar data I had been manually scraping...
### 7.7.19 : Added Workflow markdown file.
Might be extraneous, but it outlines basically getting the raw data, using a couple of tools in the MFL package to tidy things up, and mentioning further follow up in other tools (Tableau, etc).
### 6.26.19 : Renamed functions, minor cleanup of documentation. 
### 6.3.19 : Cleaned up existing code, added ReturnTopN function.
### 5.30.19 : Uploaded the initial MFL package which includes the first few functions to clean and parse the raw MFL data. If they work the way they should (ha!) the functions will: 
1. clean the raw data from MFL,
2. return the top n players in each position,
3. return the top n players on each team,
4. flatten the data into a tidy dataset.

Im working on the function for returning top n players by team as well. Then I can move on to more of the analytics.
