#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input('Digite alguma coisa: ')
print('O tipo primitivo é ', type(a))
print('Só tem espaços? ',a.isspace())
print('É um número? ',a.isalnum())
print('É alfabético? ',a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Está em maiúsculas? ',a.isupper())
print('Está em minúsculas? ',a.islower())
print('Está capitalizada? ',a.istitle())  #nem maiúscula nem minúscula totalmente, misturado
