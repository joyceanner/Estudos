#Conversão de moedas 
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.87
euro = real / 5.28
print('Com R${:.2f} você pode comprar US${:.2f} e €${:.2f}'.format(real, dolar, euro))
