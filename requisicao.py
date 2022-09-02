import json
import requests
import time

def checagempokemon(pokemon):
    try:
        req = requests.get('https://pokeapi.co/api/v2/pokemon/'+ pokemon)
        info = json.loads(req.text)
        ataque = info['stats'][1]['base_stat']
        defesa = info['stats'][2]['base_stat']
        return ataque, defesa
    except:
        print('Não foi possivel encontrar seu Pokemon')
        return False

sair = False
while not sair:
    start = input('Você deseja iniciar uma batalha Pokemon? Sim ou Não: ')
    if start == 'não' or start == 'nao':
        sair = True
    else:
        duelista1 = input('Primeiro duelista Escolha seu Pokemon: ')
        duelista2 = input('Segundo duelista Escolha seu Pokemon: ')
        pokestats1 = checagempokemon(duelista1)
        pokestats2 = checagempokemon(duelista2)
        ataque1 = pokestats1[0]
        defesa1 = pokestats1[1]
        ataque2 = pokestats2[0]
        defesa2 = pokestats2[1]
        print('Seu Pokemon',duelista1, 'possui',ataque1, 'de ataque e',defesa1, 'de defesa.')
        print('Seu Pokemon adversario', duelista2, 'possui',ataque2, 'de ataque e',defesa2, 'de defesa.')
        print('Iniciando Batalha Pokemon')
        print('.')
        time.sleep(3)
        print('..')
        time.sleep(5)
        print('...')
        if ataque1 > defesa2:
            resultado = 'O '+ duelista1+' venceu está batalha.\n'
            print(resultado)
        else:
            resultado = 'O '+duelista2+' venceu está batalha.\n'
            print(resultado)

        with open('resultados_batalhas_pokemon.txt','a') as arquivo:
            arquivo.write(resultado)