import threading,time,random

class Piloto(threading.Thread):
    def __init__(self,nomePiloto):
        threading.Thread.__init__(self)
        self.nomePiloto=nomePiloto
        self.tempoCorrida=0
    def run(self):
        tempoVolta=0
        for i in range(1,66):
            print("O piloto ",self.nomePiloto," deu a volta ",i)
            tempoVolta=random.random()
            self.tempoCorrida+=tempoVolta
            time.sleep(tempoVolta)
        print("O piloto ",self.nomePiloto, " terminou a sua corrida!")

piloto01=Piloto("Felipe Massa")
piloto02=Piloto("Lewis Hamilton")

piloto01.start()#Começou a executar
piloto02.start()#Começou a executar, independente do primeiro

piloto01.join()
piloto02.join()

if piloto01.tempoCorrida>piloto02.tempoCorrida:
    print("O vencedor foi ",piloto02.nomePiloto)
elif piloto01.tempoCorrida<piloto02.tempoCorrida:
    print("O vencedor foi ",piloto01.nomePiloto)
else:
    print("Foi empate!")




