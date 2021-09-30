# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras ao todo (sem considerar os espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip() # Remove todos os espaços inúteis no início e no final da string.
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')) # Quantidade de letras no nome menos os espaços entre os nomes.
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
      

      
