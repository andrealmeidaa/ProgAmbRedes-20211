import socket
import struct
GRUPO_MULTICAST='224.1.1.1'
PORTA_MULTICAST=5007
ENVIAR_TODOS=False

#AF_INET=Família de Protocolo de Internet
#SOCK_DGRAM = socket do tipo Datagrama
#IPPROTO_UDP = Protocolo UDP
socketMulticast=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
#Configuração para permitir que o SO atributa diferentes portas para o mesmo socket, com o mesmo endereço
socketMulticast.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

if ENVIAR_TODOS:
    socketMulticast.bind(('',PORTA_MULTICAST)) #Recebe mensagem de qualquer grupo
else:
    socketMulticast.bind((GRUPO_MULTICAST,PORTA_MULTICAST)) #Recebe mensagem de um grupo específico
'''Monta um uma estrutura ip_mreq para incluir o socket no grupo, 
assim adicionamos em formato bytstring o endereço IP do grupo multicast e o endereço da inteface de rede
'''
ip_mreq=struct.pack('4sl',socket.inet_aton(GRUPO_MULTICAST),socket.INADDR_ANY)
#Com o ip_mreq criado fazemos a inclusão do socket dentro do grupo multicast
socketMulticast.setsockopt(socket.IPPROTO_IP,socket.IP_ADD_MEMBERSHIP,ip_mreq)

#Abre loop infinito para ficar ouvindo as mensagens
while True:
    print(socketMulticast.recv(1024).decode())
