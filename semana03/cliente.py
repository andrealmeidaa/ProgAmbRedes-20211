import socket
host='127.0.0.1'
port=5000
soqueteCliente=socket.socket()
soqueteCliente.connect((host,port)) #Cliente se conecta na mesma porta e host do servidor
mensagem=input("->")
while mensagem!='q':
    soqueteCliente.send(mensagem.encode()) #Envia a mensagem em formato de bytes
    mensagemServidor=str(soqueteCliente.recv(1024).decode()) #Recebe a mensagem do servidor
    print("Mensagem recebida do servidor: {}".format(mensagemServidor))
    mensagem=input("->")

soqueteCliente.close()