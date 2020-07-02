##Desafio 15
#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Informe a quantida de km: ' ))
dias = int(input('Informe a quantidade de dias: '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é {:.2f}.'.format(pago))