#Faça um algoritmo que leia o salário fico e um vendedor e total de vendas efetuadas por ele no mês. Sabe-se que ele ganha 15% de comissão sobre as vendas efetuadas. O programa deverá mostrar o valor do salário ficxo, a comissçao que ele ganhará e o salário final.
salario =  float(input('Informe seu salário: R$ '))
vendas =  float(input('Informe o total de vendas no mês:'))
comissao = (vendas *15/100)
total = salario + comissao
print('O seu salário fixo é de R${}, sua comissão este mês foi de R${} e o seu salário final é {}. Bom trabalho!'.format(salario, comissao, total))
