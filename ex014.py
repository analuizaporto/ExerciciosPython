# Digite um número e calcule sua raiz quadrada.

import math #importa todas as possibilidades
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f)'.format(num, raiz))

#Outra opção é importar apenas a função que a gente vai usar, no caso sqrt:

from math import sqrt
num = int(input('Digite um número: '))
raiz = sqrt(num) #-> Não precisa declarar math quando importa a função diretamente.
print('A raiz de {} é igual a {:.2f)'.format(num, raiz))

