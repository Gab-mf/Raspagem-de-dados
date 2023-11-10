import requests
from bs4 import BeautifulSoup
import pandas as pd

# Link do mercado livre
url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

# concatenando o link com o nome do produto
response = requests.get(url_base + produto_nome, verify=False)

site = BeautifulSoup(response.text, 'html.parser')

# Listando todos os produtos
produtos = site.find_all('div', class_="andes-card ui-search-result ui-search-result--core andes-card--flat andes-card--padding-16")

dados_produtos = []

#Loopando todos os produtos e pegando o título, link e preço
for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    link = produto.find('a', attrs={'class':'ui-search-link'})
    real = produto.find('span', attrs={'class':'andes-money-amount__fraction'})
    centavo = produto.find('span', attrs={'class':'andes-money-amount__cents andes-money-amount__cents--superscript-24'})

    print('titulo ', titulo.text)
    print('Link', link['href'])
    print('Real', real.text)

    if titulo and link and real:
        dados_produtos.append({
            'Título': titulo.text.strip(),
            'Link': link['href'],
            'Preço': f"{real.text.strip()}.{centavo.text.strip()}" if centavo else real.text.strip()
        })

# organizando os produtos em um dataframe
tabela_miband = pd.DataFrame(dados_produtos)
print(tabela_miband)

# convertendo o dataframe em uma planilha do excel
tabela_miband.to_excel("Preços miband.xlsx", index=False)