import pandas as pd
import xlrd
import copy

def get_data():
    df_games = pd.read_excel('nfl_games_all.xlsx', sheet_name='2019 Games')
    df_elo = pd.read_excel('elo_data.xlsx')

    df_weekly_list = []
    for i in range(1, 18):
        df_weekly_list.append(df_games.loc[df_games['Week'] == i])
    return df_games, df_weekly_list, df_elo

def expand_games(df):
    winners = df['Winner']
    losers = df['Loser']
    df1 = copy.copy(df)
    df1['Team'] = winners
    df1['Opponent'] = losers
    df2 = copy.copy(df)
    df2['Team'] = losers
    df2['Opponent'] = winners
    return pd.concat([df1,df2])

def add_win_probs(df, df_elo):
    win_prob_list = []
    for index, row in df.iterrows():
        team = row.loc['Team']
        team_elo = df_elo.loc[df_elo['Team'] == team]['Elo'].to_list()[0]
        opponent = row['Opponent']
        opp_elo = df_elo.loc[df_elo['Team'] == opponent]['Elo'].to_list()[0]
        elo_diff = team_elo - opp_elo
        win_prob = 1/((10**(-elo_diff/400))+1)
        win_prob_list.append(win_prob)
    df['Win Prob'] = win_prob_list



def construct_dfs():
    df_games, df_weekly_list, df_elo = get_data()
    df_list = []
    for df in df_weekly_list:
        df_list.append(expand_games(df))
    for df in df_list:
        add_win_probs(df, df_elo)
    return df_list





if __name__ == '__main__':
    df_list = construct_dfs()
    for i in range(len(df_list)):
        df_list[i].to_csv(f'weekly_game_data/week_{i + 1}.csv', index = False)
