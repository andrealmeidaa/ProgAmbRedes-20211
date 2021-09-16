from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

browser=Chrome(options=chrome_options)

browser.get('https://www.premierleague.com/tables')
wait=WebDriverWait(browser,2)

soup=BeautifulSoup(browser.page_source,'lxml')
try:
    
    tabela=soup.find('tbody',class_='tableBodyContainer isPL')
    
    linhas=tabela.select('tr[data-position]')
    
    for linha in linhas:
        colunas=linha.find_all('td')
        time=colunas[2].find('span',class_='long')
        print(time.get_text())
except Exception as error:
    print("Erro: ",error)
    browser.quit()

browser.quit()