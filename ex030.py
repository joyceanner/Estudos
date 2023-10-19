#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
#obs: se o ano for dividido por 4 e der zero isso significa que é bissexto e também não pode ser dividido por 100 ou o ano ser dividido por 400.
from datetime import date
ano = int(input('Que ano deseja analisar? Coloque 0 para analisar o ano atual:'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
        print('O ano {} é BISSEXTO'.format(ano))
else:
        print('O ano {} NÃO é BISSEXTO'.format(ano))
