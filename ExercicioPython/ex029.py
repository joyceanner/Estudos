#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dis = float(input('Insira a distância da viagem em KM:'))
if dis <= 200:
    calc = dis * 0.50
if dis > 200 :
    calc = dis * 0.45
print('Sua passagem será no valor de: R$ {:.2f}'.format(calc))

