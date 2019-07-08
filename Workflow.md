# OKFL Data Prep and Analysis

## Download raw data
These files are what I downloaded from the MFL website (https://www.MyFantasyLeague.com).
- OKFL Top 500 Offense 2016.csv
- OKFL Top 500 Offense 2017.csv
- OKFL Top 500 Offense 2018.csv

### Raw data format
Data is in a wide table format with each row representing one player. There are a few categorical fields and then a series of columns representing the 17 weeks' points.

field | description
--- | ---
\# | row index
PLAYER | (player name, team, position) space separated string, team and position are 3 and 2 letter abbreviations
PTS | total points scored for the season
AVG | average points scored for the season
1 - 17 | weekly point totals, bye week indicated by 'B', did not play indicated by a blank
STATUS | OKFL team name and player status
BYE | player bye week

## Clean and parse data
Using the MFL package:
1. Run Prep() on the raw data file; outputs a dataframe.
   Prep does some minor cleanup of the raw data file and appends the season (input at runtime) to each row. 
      * The PLAYER field is separated into name, team, and position.
      * STATUS field is parsed to return just the OKFL team name.
      * Bye and blank weeks are replaced with np.NaN.
      * Creates new columns with precalculated statistics (min, max, median, mean, stdev, games played, total points).
      * Season column is added based on input parameter.
      * Removes columns (#, PLAYER, PTS, STATUS, BYE).
2. Optionally use ReturnTop(), ReturnTopN(), ReturnTopTeam() to create smaller datasets; outputs a dataframe with identical shape.
   Each of these functions allows the user to subset the output of Prep() by the top n players by position or team.
3. Use Flatten() on these dataframe(s) to create a tidy (flat) dataset.
   Flatten converts the output of Prep() into a tidy (tall) dataframe.
      * Removes all aggregate data points.
      * Transposes data, creating two new fields from the weekly point totals (week, points).
4. Further analysis using tool of your choice.
   I have continued to do further research using Python and some seaborn visualizations. I have also used the flat files as raw data in [Tableau](https://public.tableau.com/profile/richard.parker#!/vizhome/OKFLDashboard/OKFLStory). Would like to do similar in PowerBI.
