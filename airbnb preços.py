import requests
from bs4 import BeautifulSoup
import pandas as pd

# Link acomodações em Parati

url_base = "https://www.airbnb.com.br/s/Paraty-~-RJ/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-12-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&query=Paraty%20-%20RJ&place_id=ChIJkbRoazwOnQARlCvcUdzzh_Q&date_picker_type=calendar&source=structured_search_input_header&search_type=autocomplete_click"

response = requests.get(url_base, verify=False)

site = BeautifulSoup(response.text, 'html.parser')

# lista de acomodações da página pesquisada
acomodacoes = site.find_all('div', class_="fwts1ay dir dir-ltr")

dados_acomodacoes = []

# fazendo um loop com todas as acomodações para pegar titulo, descrição, avaliação, preço e link
for acomodacao in acomodacoes:
    titulo = acomodacao.find('div', attrs={'class':'t1jojoys dir dir-ltr'})
    descricao = acomodacao.find('span', attrs={'class':'t6mzqp7 dir dir-ltr'})
    avaliacao_media = acomodacao.find('span', attrs={'class':'t1a9j9y7 r4a59j5 dir dir-ltr'})
    preco = acomodacao.find('span', attrs={'class':'_1y74zjx'})
    link = acomodacao.find('a', attrs={'class':'l1ovpqvx bn2bl2p dir dir-ltr'})

    print('titulo ', titulo.text)
    print('Descrição', descricao.text)
    print('Avaliação média', avaliacao_media.text)
    print('Preço', preco.text)
    print('Link', link.text)

    if titulo and link and descricao and avaliacao_media and preco and link:
        dados_acomodacoes.append({
            'Título': titulo.text.strip(),
            'Descrição': descricao.text.strip(),
            'Avaliação média': avaliacao_media.text.strip(),
            'Preço': f"{preco.text.strip()}.{preco.text.strip()}",
            'Link': link['href']
        })
# Organizando as acomodações em um dataframe
acomodacoes_airbnb = pd.DataFrame(dados_acomodacoes)
print(acomodacoes_airbnb)

# Convertendo o dataframe numa planilha excel
acomodacoes_airbnb.to_excel("Acomodações airbnb.xlsx", index=False)