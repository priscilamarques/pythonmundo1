# Desafio 2
# Faça um programa que leia algo pelo teclado e mostre na tela seu tipo primitvo
# e todas as informações possíveis sobre ele.
a = input('Digite algo: ')
print('É numérico?', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('Está capitalizada?', a.istitle())
print('Está em maiúscula? ', a.isupper())
print('Está em minúscula? ', a.islower())
