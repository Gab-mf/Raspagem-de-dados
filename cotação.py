import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook


# Função para obter cotação de moeda
def obter_cotacao_moeda(url, moeda):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }

    # Desabilitar verificação SSL
    requisicao = requests.get(url, headers=headers, verify=False)

    soup = BeautifulSoup(requisicao.text, 'html.parser')

    # Tentar encontrar o elemento desejado
    cotacao_element = soup.find('span', {'class': 'DFlfde SwHCTb'})

    if cotacao_element:
        cotacao = cotacao_element.text
        print(f'Cotação de {moeda}: {cotacao}')
        return cotacao
    else:
        print(f'Erro: Não foi possível encontrar a cotação de {moeda}. Verifique a estrutura HTML do site.')
        return None


# URL da cotação de Dólar e Euro no Google Finance
url_dolar = 'https://www.google.com/search?q=cotacao+dolar'
url_euro = 'https://www.google.com/search?q=cotacao+euro'

# Obter as cotações
cotacao_dolar = obter_cotacao_moeda(url_dolar, 'Dólar')
cotacao_euro = obter_cotacao_moeda(url_euro, 'Euro')

# Se as cotações foram obtidas com sucesso, escrever no Excel
if cotacao_dolar is not None and cotacao_euro is not None:
    # Criar um arquivo Excel
    workbook = Workbook()
    sheet = workbook.active

    # Escrever os dados no Excel
    sheet['A1'] = 'Moeda'
    sheet['B1'] = 'Cotação'
    sheet['A2'] = 'Dólar'
    sheet['B2'] = cotacao_dolar
    sheet['A3'] = 'Euro'
    sheet['B3'] = cotacao_euro

    # Salvar o arquivo Excel
    workbook.save('cotacoes_moedas.xlsx')