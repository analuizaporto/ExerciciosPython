# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200km e R$0,45 
# para viagens mais longas. 

d = float(input('Quantos kms de distância até o seu destino? '))
curta = d * 0.50
longa = d * 0.45
if d <=200.0:
  print('O valor da viagem é {:.2f}'.format(curta))
else:
  print('O valor da viagem é {:.2f}'.format(longa))
