# OKFL Fantasy Football Fun
This repo contains the MFL package and other documentation to support my fantasy football Tableau dashboard. The workflow is saved in a Jupyter notebook (<i>OKFL 2018 Post Season Dashboard.ipynb</i>) which relies on the MFL package as well as a couple of other basic Python libraries. The initial workflow focuses on one season, 2018, but long term goals are to:
- pull and combine data for multiple seasons,
- create a standalone 2019 dashboard modeled on this, updated weekly as the season goes on,
- create separate statistical player analysis workflow in Python, leveraging more Seaborn visualizations and eventually moving some to Tableau or PowerBI.

## Workflow Outline
1. Init routines - import libraries, create any manual lists
2. ETL - use API functions to pull multiple sets of data from the MyFantasyaLeague website, clean and combine this data into new tables
3. Export - export 4 new flat files for use by the Tableau dashboard

## Update Log
### 8.14.19 : Repo admin and cleanup
Deprecating the old workflow, working on replacing it with new flow pushing cleaned data to Tableau.
- <i>Original Project Goals</i>
- <i>OKFL 2018 Post Season Dashboard.ipynb</i>
### 8.4.19 : Broke package up into separate files
So maybe Im getting too fancy, but I separated code into two files in the package. One is for the code dealing specifically with the API calls. The other contains the original utility functions I used to clean and manipulate the old scraped data. The plan is to get all the important API stuff built out and retool the utilities to work on the API data instead. I also added the functions to get PlayerScores() and WeeklyResults().

Im moving towards having the OKFL dashboard be a separate project that I can share with the rest of the league. As such, I want to get it tidied up and an update process in place before the season starts.
### 7.24.19 : Added new Jupyter Notebook, initial goals completed!
I added a new notebook for my script that pulls data from the MFL website via API, cleans and blends it, then spits it back out as a flat file for Tableau. The dashboard is available [here](https://public.tableau.com/views/2018PostSeason/2018Overview?:embed=y&:display_count=yes&:origin=viz_share_link). There are more pieces of the API that I need to add into the MFL package, and I will probably rework the entire thing to be based off of the API calls rather than my primitive copypasta :D
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
