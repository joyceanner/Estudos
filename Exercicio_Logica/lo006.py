#Faça um algoritmo que solicite o preço inicial do veículo desejado, sem incluir os acessórios. A seguir a lista dos acessórios possíveis de acrescentar e os respectivos preços: 1 AR CONDICIONADO -3000 2 DIREÇÃO HIDRAULICA - 1500 ALARME -500 ALTO-FALANTE - 1000. O algoritmo ddeverá perguntar se deseja incluir cada um dos acessórios acima, pedindo ao usuário para digitar q se sua resposta for "sim" e 2 se sua resposta for "não".
totacessorios = 0
contacessorios = 0

print('***** GOMES VEÍCULOS *****')
inicial = int(input('Qual é o valor do veículo sem acessórios? R$'))

#Acessórios
print('---ACESSÓRIOS---"')
print('Instrução: Digite 1 para "sim" e 2 para "não" e pressione ENTER')

resposta = int(input('Tem ar-condicionado?'))
if resposta == 1:
    totacessorios + 3000
    contacessorios + 1

resposta = int(input('Tem Direção hidraulica?'))
if resposta == 1:
    totacessorios + 1500
    contacessorios + 1    

resposta = int(input('Tem alarme?'))
if resposta == 1:
    totacessorios + 500
    contacessorios + 1

resposta = int(input('Tem auto-falantes?'))
if resposta == 1:
    totacessorios + 1000
    contacessorios + 1

final = inicial + totacessorios
print('Preço inicial: R${}'.format(inicial))
print('Quantidade de acessórios : {}'.format(contacessorios))
print('Valor total dos acessórios: R${}'.format(totacessorios))
print('Preço final: R${}'.format(inicial+totacessorios))

#Exercício não concluído.
