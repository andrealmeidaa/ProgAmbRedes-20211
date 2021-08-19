import socket

host="127.0.0.1" #Indica que é o localhost
port=5050
soquete=socket.socket() #Cria uma referência para um objeto socket
soquete.bind((host,port)) #liga o socket na porte e host especificados na tupla
soquete.listen(1) #Entra em modo de escuta, para 1 conexão
print("Aguardando Conexão....")
#Nesse ponto, o socket fica aguardando chegar uma conexão. Quando chegar passa para a próxima linha
conexao,enderecoCliente=soquete.accept() 
print("Conexão recebida do Cliente"+str(enderecoCliente))
while True: #Fica em laço até a conexão ser rompida
    formula=conexao.recv(1024).decode() #Se parar de receber dados, encerra o laço. Ele recebe 1024 bytes
    if not formula:
        break
    formula=str(formula) #Converte de byte para string
    mensagem=''
    try:
        resultado=eval(formula)
        mensagem='O Resultado foi {}'.format(resultado)
    except Exception:
        mensagem='Erro no processamento'
    conexao.send(mensagem.encode()) #Envia mensagem de volta para o cliente
print("Conexão Encerrada")
conexao.close()