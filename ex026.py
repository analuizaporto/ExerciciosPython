# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = nsplit()  # split fatia o nome em pedaços e joga em uma lista.
print('Muito prazer em te conhecer!')
print('Seu primeiro é nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))  # len conta o número de nomes e menos 1 porque começa com zero.
