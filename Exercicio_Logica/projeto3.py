#MEDIDOR DE VELOCIDADE
#Crie um programa que receba a velocidade do motorista e informe se ele levou multa, se sim, qual é o nível.
#Passo 1 - Definir a velocidade máxima 
#Passo 2 - Solciitar a velocidade atual 

velocidade_maxima = 80
velocidade = int(input('Informe a velocidade: '))
if velocidade <= velocidade_maxima :
    print('Não houve multa')
elif velocidade > velocidade_maxima and velocidade <= velocidade_maxima + 10:
    print('Levou multa leve')
elif velocidade >= velocidade_maxima + 11 and velocidade <= velocidade_maxima + 20:
    print('Levou multa grave')
elif velocidade > velocidade_maxima + 20:
    print('LEVOU MULTA GRAVISSÍMA')
