import re
def traduzir(palavra):
    #Cria um dicionário com os caracteres
    alfabetoLeet={
        'A':'4',
        'E':'3',
        'I':'1',
        'O':'0',
        'U':'(_)'
    }
    #Usa um for para iterar sobre o dicionário
    for letra,caractereLeet in alfabetoLeet.items():
        #O método sub da lib re faz a substituição, ignorando o case
       palavra=re.sub(letra,caractereLeet,palavra,flags=re.IGNORECASE)
    return palavra

palavraoriginal="Andre Gustavo Duarte de Almeida"
print(traduzir(palavraoriginal))
    
    