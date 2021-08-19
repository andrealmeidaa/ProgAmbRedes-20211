import socket

host='127.0.0.1'
port=5051
formato="utf-8"
tam=1024
#Conexão para recebimento de dados
servidor=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

servidor.bind((host,port))

servidor.listen(1)
print("Aguardando Conexão!")
conexao,endereco=servidor.accept()

while True:
    nomearquivo=conexao.recv(tam).decode(formato)
    if not nomearquivo:
        break
    #A função open abre um arquivo que esteja na pasta data, dentro do mesmo dir do script
    arquivo=open("data/{}".format(nomearquivo),"r")#Abre somente leitura
    conteudo=arquivo.read()#Lê o conteúdo
    conexao.send(conteudo.encode(formato))#Envia o conteúdo do arquivo
    arquivo.close()#Fecha o arquivo
    print("Arquivo {} enviado com sucesso!".format(nomearquivo))
conexao.close()