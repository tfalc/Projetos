from bs4 import BeautifulSoup
import requests

#objeto site recebe conteúdo da requisição do site
site = requests.get("https://www.globo.com").content

#objeto soup baixa o html do site
soup = BeautifulSoup(site, 'html.parser')

#transforma o html em string e imprime o html
#print(soup.prettify())

temperatura = soup.find("span", class_="menu-item-title")
print(temperatura.string)
print(soup.title.string)