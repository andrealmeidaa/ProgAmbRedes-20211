import yagmail,configparser
configuracao=configparser.ConfigParser()
configuracao.read('conf')
#No arquivo conf deve constar o usuário e a senha
sender=yagmail.SMTP(configuracao['Mail']['username'],
configuracao['Mail']['password'])

destinatarios=['andre.almeida@escolar.ifrn.edu.br','j.renato@escolar.ifrn.edu.br',
'guilhermeflorlima@gmail.com']

assunto='Aula Síncrona 14/09'

corpo='''\
<h2>Atenção</h2>
<p> Minha <a href='http://www.ifrn.edu.br'>Mensagem</a></p>
'''

sender.send(to=destinatarios,subject=assunto,contents=corpo)


print("Mensagem enviada")

