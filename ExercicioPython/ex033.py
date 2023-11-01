#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

#Cada um das retas tem que ser menos do que a soma do comprimento dos dois.
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 < r2 + r3 and r3 < r1 + r2 :
    print('Os segmmentos acima PODEM FORMAR triângulo.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo.')