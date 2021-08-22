import socket

#Cliente é implementado a qualquer cliente do tipo socket

HOST='127.0.0.1'
PORT=2345

clienteSocket=socket.socket()
clienteSocket.connect((HOST,PORT))
mensagem=input("->")
while mensagem!='q':
    clienteSocket.send(mensagem.encode())
    mensagemRetorno=clienteSocket.recv(1024).decode()
    print("Resposta do servidor: "+mensagemRetorno)
    mensagem=input("->")
clienteSocket.close()