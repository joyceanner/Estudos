# FATORIAL DE UM NÚMERO
#Crie um programa que recebe um número e imprima o seu fatorial
#Passo 1 - Solicitar um número (deve ser um número positivo e inteiro)
#Passo 2 - loop de 1 a numero
#Passo 3 -Calcular o valor inicial * fatorial

numero = int(input('Digite um número: '))
if numero > 0:
    fatorial = 1
    for item in range(1,numero +1):
        fatorial = fatorial * item
print(fatorial)
