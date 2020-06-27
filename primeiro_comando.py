nome = input('Qual seu nome? ')
idade = input('Qual sua idade? ')
peso = input('Qual seu peso? ')

print(nome, idade, peso)

##Desafio 1
#Crie um script Python que leia o nome da pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

nome = input('Qual o seu nome? ')
print(f'Olá, {nome}! Prazer em te conhecer!')

##Desafio 2
#Crie um script Python que leia o dia, mës e ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada

dia = input('Digite o dia do seu nascimento: ')
mes = input('Digite o mês do seu nascimento: ')
ano = input('Digite o ano do seu nascimento: ')
print(f'Você nasceu no dia {dia} de {mes} do ano de {ano}. Correto?')

##Desafio 3
#Crie um script Python que leia dois números e tente mostrar a soma entre eles.

n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
soma = n1 + n2
print(f'A soma é {soma}')
