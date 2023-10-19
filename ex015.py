#Crie um programa que calcule a quilometragem e dias rodados de um carro alugado e retorne o valor a ser pago.
km = float(input('Quantos Kms você rodou com o carro?'))
dias = float(input('Quantos dias você rodou com o carro?'))
diaria = dias * 60
gasto = km * 0.15
total = diaria + gasto
print('O total a pagar é de {}'.format(total))