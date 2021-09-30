# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250 calcule um aumento de 10%. 
# Para os infereiores ou iguais o aumento é de 15%.

salario = float(input('Digite o seu salário: '))
maior = salario * 0.1
menor = salario * 0.15
if salario > 1250:
  print('O aumento do seu salário foi de R${:.2f}'.format(maior))
else:
  print('O aumento do seu salário foi de R${:.2f}'.format(menor))
