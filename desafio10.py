##Desafio 10
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#Considerar dólar no valor de 3.27

real = float(input('Quanto de dinheiro vocë tem na carteira: R$ '))
dolar = real/3.27


print('Com R${:.2f} você pode comprar US${:.2f} dolares.'.format(real,dolar))