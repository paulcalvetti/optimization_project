import pandas as pd
import xlrd


df = pd.read_excel('nfl_games_all.xlsx', sheet_name='2019 Games')
print(df)