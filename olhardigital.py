from bs4 import BeautifulSoup
import requests
import pandas as pd
from openpyxl import Workbook

URL = 'https://olhardigital.com.br/'
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
HEADERS = ({'User-Agent': user_agent, 'Accept-Language': 'pt-BR'})
webpage = requests.get(URL, headers=HEADERS)

soup = BeautifulSoup(webpage.content, "html.parser")
cont = 0
cont2 = 1
cont3 = 5

titulos = []
links = []
for i in range(4):
    card_principais = soup.find("a", attrs={"class": f"cardV2 cardV2-incover feat{cont}"})
    titulo = card_principais['title']
    link = card_principais['href']
    titulos.append(titulo)
    links.append(link)
    cont = cont + 1

ultima_materias_card = soup.find("a", attrs={"class": "cardV2 cardV2-incover list-post-0"})
tituloc = ultima_materias_card['title']
linkc = ultima_materias_card['href']
titulos.append(tituloc)
links.append(linkc)

for i in range(4):
    ultimas_materias = soup.find("a", attrs={"class": f"cardV2 cardV2-tarja list-post-{cont2}"})
    titulo = ultimas_materias['title']
    link = ultimas_materias['href']
    titulos.append(titulo)
    links.append(link)
    cont2 = cont2 + 1

for i in range(2):
    materia_do_lado = soup.find("a", attrs={"class": f"cardV2 cardV2-tarja cardV2-incover-desktop list-post-{cont3}"})
    cont3 = cont3+1
    titulo = materia_do_lado['title']
    link = materia_do_lado['href']
    titulos.append(titulo)
    links.append(link)


card_vertical = soup.find_all("a", attrs={"class": "cardV2 cardV2-vertical"})
for item in card_vertical:
    titulob = item['title']
    linkb = item['href']
    titulos.append(titulob)
    links.append(linkb)

olhadigital_df = pd.DataFrame({"Título": titulos, "Link": links})
olhadigital_df.to_excel("olhadigital.xlsx", header=True, index=False)
