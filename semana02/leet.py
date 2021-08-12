import re
def traduzir(palavra):
    alfabetoLeet={
        'A':'4',
        'E':'3',
        'I':'1',
        'O':'0',
        'U':'(_)'
    }
    
    for letra,caractereLeet in alfabetoLeet.items():
       palavra=re.sub(letra,caractereLeet,palavra,flags=re.IGNORECASE)
    return palavra

palavraoriginal="Andre Gustavo Duarte de Almeida"
print(traduzir(palavraoriginal))
    
    