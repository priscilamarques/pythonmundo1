##Desafio 12
#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto custava R${:.2f}, na promoção com desconto de 5% custará R${:.2f}'.format(preco,novo))

