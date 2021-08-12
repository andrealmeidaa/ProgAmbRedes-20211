import locale
import calendar

def data_extenso(data):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')#Defini a localidade
    dia,mes,ano=data.split('/')#Parte a data em três partes especifícas
    #A data formatada é gerada com concatenação. Poderiamos usar a função format também
   # data_formatada=dia+' de '+calendar.month_name[int(mes)].capitalize()+' de '+ano
   #Data formatada com a função format
    data_formatada="{} de {} de {}".format(dia,calendar.month_name[int(mes)].capitalize(),ano)
    return data_formatada
print(data_extenso('12/08/2021'))
