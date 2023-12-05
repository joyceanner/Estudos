#Chute um número
#Escreva um programa que ao iniciar gere um valor aleatório de 1 a 10 e permite que o usuário chute um número até que o valor acertar o valor gerado no inicio.
#Passo 1 - Definir um valor aleatório
#Passo 2 - Solicitar um número de 1 a 10 ao usuaário
import random

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um número de 1 a 10: '))
    if chute > valor_aleatorio:
        print("Chutou alto!")
    elif chute < valor_aleatorio:
        print('Chutou baixo!')
    elif chute == valor_aleatorio:
        acertou = True
        print('Acertou! LOL')    
        