import socket,threading #Importa a lib thread
HOST='127.0.0.1'
PORT=2345
class ClientThread(threading.Thread): #Cria a classe que herda de threading.Thread
    def __init__(self,enderecoCliente,socketCliente): #Construtor que recebe um endpoint e a referência ao socket
        threading.Thread.__init__(self)
        self.csocket=socketCliente
        self.enderecoCliente=enderecoCliente
        print("Conexão recebida de ",enderecoCliente)
    def run(self): #Método da classe Thread que é executado quando o thread é iniciado
        mensagem=""
        contadorMensagens=0
        while True:
            mensagem=self.csocket.recv(1024).decode()
            if not mensagem:
                break
            print("Recebeu de ",self.enderecoCliente," a mensagem: ",mensagem)
            contadorMensagens+=1
            mensagemRetorno="Tudo ok pela {} vez".format(contadorMensagens)
            self.csocket.send(mensagemRetorno.encode())
        print("Cliente ",self.enderecoCliente, " desconectado!")

servidor=socket.socket()
servidor.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEPORT,1) #Permite reuso da porta, para receber múltiplas conexões
servidor.bind((HOST,PORT))
print("Aguardando Conexões")
while True:
    servidor.listen(1)#Abre novo espaço para receber conexão
    clienteSocket,enderecoCliente=servidor.accept()#Aguarda receber uma conexão
    threadCliente=ClientThread(enderecoCliente,clienteSocket)#Cria um objeto da classe ClientThread
    threadCliente.start()#Inicializa o Thread e continua no loop para receber novas conexões
servidor.close()