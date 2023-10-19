#Condições
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Qual foi a velocidade do carro?'))
if vel >80.0 :
    print('Você ultrapassou os limites de velocidade')
    mt = (vel - 80) * 7
    print('Sua multa é no valor de {}.'.format(mt))
else:
    print('Você não tem nenhuma dívida.')

