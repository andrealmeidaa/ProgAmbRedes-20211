import socket

host='127.0.0.1'
port=5051
formato="utf-8"
tam=1024

cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

cliente.connect((host,port))#Conecta no endpoint do socket servidor

while True:
    nomearquivo=input("Informe o arquivo desejado:")
    if nomearquivo=='q':
        break
    cliente.send(nomearquivo.encode())#Envia o nome do arquivo a ser aberto
    arquivo=open("data/recebido/{}".format(nomearquivo),"w")#Abre/cria um arquivo dentro data/recebido
    conteudo=cliente.recv(tam).decode(formato)#Recebe o conteudo do arquivo, limitado a 1024 bytes
    arquivo.write(conteudo)#Escreve o conteúdo recebido no arquivo
    arquivo.close()#Fecha o arquivo
    print("Arquivo salvo com sucesso!")
cliente.close()