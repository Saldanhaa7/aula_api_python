import requests
import json

cotacao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacao = cotacao.json()
cotacao_dolar = float(cotacao['USDBRL'] ['bid'])
valor = int(input('valor em dólar '))
valor_total = valor*cotacao_dolar
#print(type(cotacao_dolar))
#print(type(valor))
#print(valor_total)
#print(cotacao)
if valor == 0:
    print('valor inválido, por favor digite outro')
if valor == 1:
    print(str(valor) + ' dólar vale ' + str(cotacao_dolar) + ' reais')
if valor > 1:
    print(str(valor) + ' dólares vale ' + str(valor_total) + ' reais')