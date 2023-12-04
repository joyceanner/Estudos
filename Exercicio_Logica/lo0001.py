#VALOR POR HORA
#Escreva um programa que leia informe o valor da hora trabalhada de acordo com o salário e quantidade de horas do funcionário.
#Passo 1 - Perguntar quanto é o salário
#Passo 2 - Peeguntar quantas horas trabalha ao mês
#Passo 3 - Dividir o salário pela quantidade de horas
#Passo 4 - Retornar o resultado.
salario = int(input('Qual é o seu salário ? R$'))
horas = int(input('Quantas horas você trabalha por mês?'))
resultado = salario / horas
print('O valor de sua hora trabalhada é {}.'.format(resultado))