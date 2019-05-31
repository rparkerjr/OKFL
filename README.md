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

## Questions to Answer
Aside from the coding goals I listed above, I did want to answer a few specific questions about the data:
1. Are certain NFL teams better sources of players? IE, do certain teams regularly have high-scoring players while others are dogs?
2. How do the individual positions stack up against each other when it comes to player scores?
3. Are there discernible tiers of players? Does it make sense to focus on players within a tier vs. specific players?

## Update Log
5.30.19 : Uploaded the initial MFL package which includes the first few functions to clean and parse the raw MFL data. If they work the way they should (ha!) the functions will: 
1. clean the raw data from MFL,
2. return the top n players in each position,
3. flatten the data into a tidy dataset.

Im working on the function for returning top n players by team as well. Then I can move on to more of the analytics.
