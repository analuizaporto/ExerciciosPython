# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Digite quantos metros: '))
cm = m * 100
mm = m * 1000
print('{} metros equivale a {} centímetros e {} milímetros'.format(m, cm, mm))
