#Exibir maior dos dois valores
#Passo 1 - Solicitar o primeiro valor
#Passo 2 - Solicitar o segundo valor
#Passo 3 - Comparar os dois valores
#Passo 4 - Retornar o maior dos dois valores
primeiro = int(input('Digite o primeiro valor:'))
segundo = int(input('Digite o segundo valor:'))
if primeiro > segundo :
    print('O primeiro valor foi o {} e é o maior.'. format(primeiro))
else:
    print('O segundo valor foi o {} e é o maior.'.format(segundo))

