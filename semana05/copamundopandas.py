import requests,json
import pandas as pd

requisicao=requests.get('https://world-cup-json-2018.herokuapp.com/matches')
dados=json.loads(requisicao.text)

dataFrame=pd.json_normalize(dados)

dataFrameTimes=dataFrame.groupby('home_team_country')['home_team.goals'].sum()+dataFrame.groupby('away_team_country')['away_team.goals'].sum()

print(dataFrameTimes)