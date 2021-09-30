# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite quantos km foram percorridos: '))
dias = int(input('Por quantos dias o carro foi alugado? '))
preço = (60 * dias) + (0.15 * km)
print('O preço a pagar por {}km percorridos e {} dias alugados é R${}'.format(km, dias, preço))
