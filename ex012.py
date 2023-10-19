#Crie um programa que solicite o valor do produte e calcule-o após determinado desconto.
preço = float(input('Qual é o preço do produto? R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
