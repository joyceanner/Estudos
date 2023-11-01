#Retornar a parte inteira de um número real.
import math
num = float(input('Digite um número real:'))
r = math.trunc(num)
print('O número {} tem a parte inteira {}.'.format(num,r))
