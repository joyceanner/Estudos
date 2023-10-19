#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

#obs: para saber se o número é par ou ímpar basta dividir o resto da divisão por 2 como no exemplo embaixo, todo número par vai dar 0 e todo número impar vai dar 1.
num = int(input('Digite um número inteiro qualquer:'))
res =  num % 2
if res == 0:
    print('O número {} é PAR'.format(num))
else:
    print('O número {} é IMPAR'.format(num))