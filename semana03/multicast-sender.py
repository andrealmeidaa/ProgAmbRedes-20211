import socket
import random
import time

GRUPO_MULTICAST='224.1.1.1'
PORTA_MULTICAST=5007

#Cria uma socket do tipo datagram e com o protocolo UDP
socketMulticast=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)
#Configura o socket para transmissão em multicast com TTL(Time to Live) de 2
socketMulticast.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,2)
#Envia a mensagem para todos os sockets dentro do grupo e porta especificados
lista=['Flamengo','Vasco','Fluminense','Botafogo']
while True:
    mensagem=str.encode('Acorda Galera do {}'.format(random.choice(lista)))
    socketMulticast.sendto(mensagem,(GRUPO_MULTICAST,PORTA_MULTICAST))
    time.sleep(2.5)