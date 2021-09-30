# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

import math
num = float(input('Digite um número: '))
i = math.trunc(num)
print('A parte inteira do {} é {}'.format(num, i))
