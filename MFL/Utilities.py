"""
MFL
Functions to clean, parse, and segment raw fantasy football player data from MyFantasyLeague. This older part of
the package is currently being redone; scripts specifically making API calls are now located in the API.py file.
The remaining cleanup and segementing scripts will be in this file. Ideally these scripts are going to be modified
so that they work on the API data. 8.2.19
"""

__author__ = "Richard Parker"
__version__ = "0.6.0"
__license__ = "GNU3.0"

# Import dependencies
import numpy as np
import pandas as pd

def Flatten(data):
    """Creates a flat, tidy dataset by pivoting the weekly scores into just two columns, week and points.
    
    Parameters
    ----------
    data : pandas.DataFrame
    
    Output
    ------
    pandas.DataFrame : tidy dataset; each record represents a player.season.week
        
    """
    
    data  = data[['player_id', 'name', 'team', 'position', 'season',
                  '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17']]
    data = data.melt(['player_id', 'name', 'team', 'position', 'season'], var_name = 'week', value_name = 'points')
    
    return data

def Prep(filename, year):
    """Clean and parse data from MFL website for use in later analysis. Data is returned in similar dimensions.
    
    Parameters
    ----------
    filename : string
        path to raw data file from MFL, in CSV format
    year : string
        year/season which this data represents, eg. '2018'
        
    Output
    ------
    pandas.DataFrame : cleaned and parsed MFL data in a wide dataframe; one record per player
    """
    
    # Check for existence first, prevent errors?
    # Begin main code block here
    df = pd.read_csv(filename)
    
    # Parse out the PLAYER field
    #   Position, Team, Name
    p = df.PLAYER

    pos = [pos[-2: ] for pos in p]
    team = [team[-6 : -3] for team in p]
    name = [name[ : -7] for name in p]

    # Clean the OKFL team field (STATUS), removing player status indicators
    df.STATUS = [t.replace(' (Q)', '') for t in df.STATUS]
    df.STATUS = [t.replace(' (O)', '') for t in df.STATUS]
    df.STATUS = [t.replace(' (I)', '') for t in df.STATUS]
    df.STATUS = [t.replace(' - IR', '') for t in df.STATUS]
    okfl_team = df.STATUS

    # Clean the weekly point totals
    df_points = df.iloc[ : , 4:-2]
    df_points.replace('B', np.NaN, inplace = True)
    df_points.replace(' ', np.NaN, inplace = True)
    df_points = df_points.astype('float', errors = 'ignore')
    
    # Aggregates, simple statistics
    games_played = df_points.notna().sum(axis = 1)
    total_points = df_points.sum(axis = 1)
    mean_points = df_points.mean(axis=1)
    median_points = df_points.median(axis = 1)
    stdev_points = df_points.std(axis=1)
    max_points = df_points.max(axis=1)
    min_points = df_points.min(axis=1)
    
    # Create new dataframe to hold cleaned data
    df2 = pd.DataFrame({'name' : name,
                        'team' : team,
                        'okfl_team' : okfl_team,
                        'position' : pos,
                        'season' : year,
                        'games_played' : games_played,
                        'total_points' : total_points,
                        'mean_points' : mean_points,
                        'median_points' : median_points,
                        'stdev' : stdev_points,
                        'max_points' : max_points,
                        'min_points' : min_points})
    
    df2 = pd.concat([df2, df_points], axis = 1)
    df2.sort_values('total_points', ascending = False, inplace = True)
    df2.insert(0, 'player_id', df2.index + 1)
    
    return df2
    
def ReturnTop(data, QB = 20, RB = 50, WR = 50, TE = 20, PK = 20):
    """Subsets full player listing by top n players in each position and returns a new dataframe.
    
    Parameters
    ----------
    data : pandas.DataFrame
        cleaned MFL data; use Prep() first
    QB, RB, WR, TE, PK : integer
        top n players by position to select
    
    Output
    ------
    pandas.DataFrame : filtered version of input
    """

    #data = pd.read_csv(data)
    data.sort_values('total_points', ascending = False)
    
    top_n = {'QB' : QB, 
             'RB' : RB, 
             'WR' : WR, 
             'TE' : TE, 
             'PK' : PK}
    
    top_data = pd.DataFrame()
    for p in top_n:
        top_data = pd.concat([top_data, data[data.position == p][0:top_n[p]]])
    
    return top_data

def ReturnTopN(data, n):
    """Returns the top n players for each offensive position. This calls ReturnTop() using n for each position value.
    
    Parameters
    ----------
    data : pandas.DataFrame
        cleaned MFL data; use Prep() first
    n : integer
        number of top players to select from each position (QB, RB, WR, TE, PK)
    
    Output
    ------
    pandas.DataFrame : filtered version of input
    """
    
    top_data = ReturnTop(data, QB = n, RB = n, WR = n, TE = n, PK = n)
    
    return top_data

def ReturnTopTeam(data, n = 10):
    """Subsets full player listing by top n teams and returns a new dataframe.
    
    Parameters
    ----------
    data : pandas.DataFrame
        cleaned MFL data; use Prep() first
    n : integer
        top n teams players per team to select
    
    Output
    ------
    pd.DataFrame : filtered version of input
    """
    
    teams = data.team.unique()
    top_data = pd.DataFrame()
    
    for t in teams:
        top_data = pd.concat([top_data, data[data.team == t][0:n]])
        #top_data = data[data.position == p][0:top_n[p]]
    
    return top_data
