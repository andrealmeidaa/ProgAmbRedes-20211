import requests,json

requisicao=requests.get('https://world-cup-json-2018.herokuapp.com/matches')

partidas=json.loads(requisicao.text)
times={}
for partida in partidas:
    #nome_time:gols_marcados(acumulando)=Gols_casa+Gols_Fora
    try:
        times[partida['home_team_country']]+=partida['home_team']['goals']
    except KeyError:
        times[partida['home_team_country']]=partida['home_team']['goals']
    try:
        times[partida['away_team_country']]+=partida['away_team']['goals']
    except KeyError:
         times[partida['away_team_country']]=partida['away_team']['goals']

for time,gols in times.items():
    print("O ",time, " marcou ",gols, " gols.")

