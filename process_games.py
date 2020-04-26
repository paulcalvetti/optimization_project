import pandas as pd
import xlrd

def get_data():
    df_games = pd.read_excel('nfl_games_all.xlsx', sheet_name='2019 Games')
    df_odds = pd.read_excel('nfl_games_all.xlsx', sheet_name='2019 Odds')

    #get list of team names
    teams = df_odds['Team'].to_list()
    return df_games, df_odds, teams

if __name__ == '__main__':
    df_games, df_odds, teams = get_data()
    print(df_games)
    print(df_odds)
    print(teams)
    print(len(teams))
