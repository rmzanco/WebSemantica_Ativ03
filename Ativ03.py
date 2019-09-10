"""
Rodrigo Malosti Zanco - 205541

Programa voltado para a aula TT001 - Web Semântica
Ativ 03 - Acesso a dados usando API (REST + JSON)
Obter os dados e realizar algum processamento nesses dados
API Utilizada: HG Weather
Funcionalidade objetiva: Escrever o nome de uma cidade, para que a API mostre a temperatura atual daquela cidade. (Cumprida!)
Proximo passo: Utilizar a chave via woeid utilizando a biblioteca woeid do python
Opcionais: método por WOEID <- colocar outra API para localizar o  WOEID (https://pypi.org/project/woeid/) e converter em Cidade, pois o App funciona melhor via woeid

"""

import requests

key = "03411ebb"
cidade = input("Digite a Cidade no seguinte formato exemplo: Campinas,SP \nNome da cidade: ")

url = 'https://api.hgbrasil.com/weather?array_limit=2&fields=city_name,temp,date,time&key=' + key + '&city_name=' + cidade
try:
    resp = requests.get(url)

    codif = resp.encoding
    conteudo = resp.content

    conteudo_str = conteudo.decode(codif)

    temp = conteudo_str[53:55]

    print("Cidade: " + cidade)
    print("Temperatura agora: " + temp + "°C")  # configurar p achar o que vem após "temp:", não pelo tamanho da string
except:
    print("Erro desconhecido. Favor contatar o desenvolvedor.")
