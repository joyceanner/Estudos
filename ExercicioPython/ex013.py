#Crie um programa que solicite o salário atual e retorne o valor atualiado após o aumento determinado.
salario = float(input('Qual é o seu salário atual? R$'))
novo = salario + (salario * 15 / 100)
print('O seu sálario que atualmente é R${}, após o aumento de 15% passará a ser R${:.2f}'.format(salario, novo))
