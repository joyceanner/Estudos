#Construa um algoritmo que leia dois valores reais e mostre o primeiro com o acrescimo de 30% e o segundo com um desconto de 25%.
primeiro = float(input("Informe um número:") )
segundo = float(input("Informe outro número:") )
acres = primeiro + (primeiro *30/100)
desc = segundo - (segundo * 25/100)



print(' O primeiro número mais 30% é igual a: {}.'.format(acres))
print(' O segundi número menos 25% é igual a: {}.'.format(desc))