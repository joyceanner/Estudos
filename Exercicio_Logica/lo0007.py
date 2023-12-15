#FAÇA UM ALGORITMO QUE PERGUNTE AO CORREDOR A SUA IDADE. O PROGRAMA DEVERÁA ESCREVER NA TELA EM QUAL CATEGORIA EKE SE ENCAIXA.

idade = int(input('Qual a sua idade?'))

if idade < 18:
    print('Sua categoria é JUNIOR.')
elif idade >= 18 and idade < 35:
    print('Sua categoria é ADULTO.')
elif idade >= 35:
    print('Sua categoria é SENIOR.')
