# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posição a letra "A" aparece a primeira vez.
# Em que posição a letra "A" aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip() 
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))  # Soma 1 porque o primeiro índice é zero.
print('A última letra A apareceu na poição{}'.format(frase.rfind('A')+1))
