# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.

salario = float(input('Digite o seu salário: '))
novo = 1.15 * salario
print('O seu novo salário é R$ {:.2f}'.format(novo))
