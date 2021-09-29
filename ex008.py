# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta 
# pinta uma área de 2m².

alt = int(input('Qual a altura da parede? '))
larg = int(input('Qual a largura da parede? '))
area = alt * larg
tinta = area / 2
print('Área da parede: {} m² e quantidade de tinta necessária: {} litros'.format(area, tinta))
