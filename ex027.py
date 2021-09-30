# Escreva um programa que leia a velocidade de um carro. Se ele ultrapasssar 80km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Qual a velocidade do carro? '))
multa = 7.0 * (velocidade - 80.0)
if velocidade > 80.0:
  print('Sua velocidade é {}, você ultrapassou o limite excedido que é de 80km/h e por isso você foi multado! A multa vai custar R${:.2f}'.format(velocidade, multa))
print('Dirija com segurança!')
