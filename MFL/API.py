"""
MFL-API
Functions to access data from MyFantasyLeague using their API. Not all API calls implemented,
only those needed most for draft analysis and powering the OKFL dashboard.

 - ByeWeeks
 - DraftResults
 - GetPlayers
 - PlayerScores
 - WeeklyResults
"""

__author__ = "Richard Parker"
__version__ = "0.6.0"
__license__ = "GNU3.0"

# Import dependencies
import numpy as np
import pandas as pd

def ByeWeeks(season = '2018', week = ''):
    """Pulls draft results from the MFL server.

    Parameters
    ----------
    season : which year do you want player information for
    week : will return the team(s) on bye that week; if left blank returns all weeks

    Output
    ------
    pandas.DataFrame : all teams and their bye weeks
    """
    json = '1'
    url = ('http://www71.myfantasyleague.com/'
           + season + 'export?TYPE=nflByeWeeks&W='
           + str(week) + '&JSON=' + json)

    data = pd.read_json(url)
    bye_weeks = pd.DataFrame.from_dict(data['nflByeWeeks'][0], orient = 'columns')

    return bye_weeks

def DraftResults(league_id = '27378', season = '2018'):
    """Pulls draft results from the MFL server.

    Parameters
    ----------
    league_id : league to pull draft results for
    season : which year do you want player information for

    Output
    ------
    pandas.DataFrame : all draft picks for the requested season including round, pick, owner_id, player_id
    """
    
    json = '1'
    url = ('http://www71.myfantasyleague.com/' 
           + season + '/export?TYPE=draftResults&L='
           + league_id + '&APIKEY=&JSON=' + json)
    
    data = pd.read_json(url)
    data = data['draftResults']['draftUnit']['draftPick']

    draft = pd.DataFrame.from_dict(data, orient = 'columns')
    draft.rename(columns = {'franchise' : 'drafted_by', 'player' : 'player_id'}, inplace = True)
    draft.drop(columns = ['comments', 'timestamp'], inplace = True)
    draft_key = (draft['round'] + draft['pick'])
    draft.set_index(draft_key, inplace = True)
    
    return draft

def GetPlayers(season = '2019'):
    """Pulls updated listing of players from the MFL server.

    Parameters
    ----------
    season : which year do you want player information for

    Output
    ------
    pandas.DataFrame : all players for the requested season including id, name, position, team
    """
    
    details = '0'
    #since = 
    #players = 
    json = '1'
    
    url = 'http://www71.myfantasyleague.com/' + season + '/export?TYPE=players&DETAILS=' + details + '&SINCE=&PLAYERS=&JSON=' + json
    
    data = pd.read_json(url)
    p = data.players.player
    players = pd.DataFrame.from_dict(p, orient = 'columns')
    players.rename(columns = {'id' : 'player_id'}, inplace = True)
    
    return players

def PlayerScores(league_id = '27378', season = '2018'):
    """Pulls weekly player scores from the MFL server. The API only pulls 1 week at a time so this script loops
    through all weeks.

    Parameters
    ----------
    league_id : league to pull matchup results for
    season : which season

    Output
    ------
    pandas.DataFrame : all weekly player scores
    """

    weeks = list(range(1, 18))
    json = '1'

    for w in weeks:
        url = ('http://www71.myfantasyleague.com/'
               + season 
               + '/export?TYPE=playerScores&L='
               + league_id
               + '&W='
               + str(w)
               + '&YEAR='
               + season
               + '&PLAYERS=&POSITION=&STATUS=&RULES=&COUNT=&JSON=' 
               + str(json))
        
        data = pd.read_json(url)
        if w == 1:
            scores = data.playerScores.playerScore
            scores = pd.DataFrame.from_dict(scores, orient = 'columns')
            scores['week'] = w
        else:
            s = data.playerScores.playerScore
            s = pd.DataFrame.from_dict(s, orient = 'columns')
            s['week'] = w
            scores = pd.concat([scores, s])
    scores['season'] = season
    scores.drop(columns = 'isAvailable', inplace = True)
    scores.rename(columns = {'id' : 'player_id', 'score' : 'points'}, inplace = True)
    scores['player_id'] = scores['player_id'].astype('str')

    return scores

def Projections(league_id = '27378', season = '2018'):
    """Pulls weekly points projections from the MFL server.

    Parameters
    ----------
    league_id : league to pull projections for
    season : which season
    # week : week to pull, blank for upcoming week

    Output
    ------
    pandas.DataFrame : all weekly matchup data including starters/non-starters, should-have-started, etc.
    """

    weeks = list(range(1, 18))
    json = '1'
    projections = pd.DataFrame(columns = ['season', 'week', 'player_id', 'proj_points'])

    for w in weeks:
        #p = pd.DataFrame(columns = ['season', 'week', 'player_id', 'proj_points'])
        url = ('http://www71.myfantasyleague.com/'
               + season + '/export?TYPE=projectedScores&L='
               + league_id + '&APIKEY=&W='
               + str(w) + '&PLAYERS=&POSITION=&STATUS=&COUNT=&JSON=' + json)

        data = pd.read_json(url)
        data = data['projectedScores']['playerScore']
        
        p = pd.DataFrame.from_dict(data)
        p.rename(columns = {'id' : 'player_id', 'score' : 'proj_points'}, inplace = True)
        p['season'] = season
        p['week'] = w
        p = p[['season', 'week', 'player_id', 'proj_points']]

        projections = pd.concat([projections, p])
    
    projections = projections.astype({'week': 'int64'}, inplace = True)  
    return projections

def WeeklyResults(league_id = '27378', season = '2018'):
    """Pulls weekly matchup results from the MFL server.

    Parameters
    ----------
    league_id : league to pull matchup results for
    season : which season

    Output
    ------
    JSON : all weekly matchup data including starters/non-starters, should-have-started, etc.
    """

    weeks = list(range(1, 18))
    json = '1'
    results = pd.DataFrame() #pd.DataFrame(columns = ['season', 'week', 'player_id', 'proj_points'])

    # iterate through weeks
    for w in weeks:
        #print('Week ' + str(w))
        url = ('http://www71.myfantasyleague.com/'
               + season 
               + '/export?TYPE=weeklyResults&L='
               + league_id
               + '&APIKEY=&W='
               + str(w)
               + '&JSON=' 
               + str(json))
        #print(url)
        data = pd.read_json(url)
        data = data.weeklyResults

        # Find number of matchups for the week and use it to limit the iterator. There are normally
        #   5 matchups per week until playoff time.
        try:
            mlen = len(data['matchup'])
        except:
            #print('Week ' + str(w) + ' No Matchups')
            continue
            
        matchups = list(range(mlen))
        # iterate through matchups
        if w == 1:
            for m in matchups:
                r = pd.DataFrame.from_dict(data['matchup'][m]['franchise'], orient = 'columns')
                r['game'] = m + 1
                r['week'] = w
                if m == 0:
                    results = r
                else:
                    results = pd.concat([results, r])
                #print(' m = ' + str(m))
            
        else:
            for m in matchups:
                r = pd.DataFrame.from_dict(data['matchup'][m]['franchise'], orient = 'columns')
                r['game'] = m + 1
                r['week'] = w
                results = pd.concat([results, r])
                #print(' m = ' + str(m))

    results['season'] = season
    results = results[['season', 'week', 'game', 'id', 'isHome', 'starters', 'nonstarters', 'optimal', 'score', 'result', 'opt_pts', 'player']]
    results = results.rename(columns = {'id' : 'owner_id', 'score' : 'team_score' })
    return results