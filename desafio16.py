#Desafio 16
##Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
from math import trunc
num = float(input('Digite um número: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num,trunc(num)))