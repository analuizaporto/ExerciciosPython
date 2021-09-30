# Faça um programa que leia um ano qualquer e mostre se o ano é Bissexto.

from datetime import date # Importando uma biblioteca de data do python.
ano = int((input('Digite um ano: . Coloque 0 para analisar o ano atual: '))
if ano == 0:
  ano = date.today().year #pega o ano atual configurado na máquina (computador)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
  print('O ano {} é bissexto'.format(ano))
else:
  print('O ano {} NÃO é BISSEXTO'.format(ano))
