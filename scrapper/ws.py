from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
# objeto site recebendo o conteudo da requisição hhtp do site...
soup = BeautifulSoup(site, 'html.parser')
# objetosoup baixando do site o html
# print(soup.prettify())
# transforma o html em strin e o print ira exibir todo o html

temperatura = soup.find('span', class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

print(temperatura.string)

print(soup.title.string)

print(soup.a)

print(soup.p.string)

print(soup.find('admin'))