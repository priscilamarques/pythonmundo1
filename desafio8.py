##Desafio 8
#Escreva um programa que leia o valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input('Quantos metros? '))
cm = m*100
mm = m*1000
print('{:.0f} metros corresponde a {:.0f} centímetros e {:.0f} milímetros '.format(m,cm,mm))