#Advinhar numero escolhido pelo computador

import random
num = random.randint(0, 10)
chute = input('Digite o numero que o computador pensou: ')

if chute == num:
    print('Você acertou!')
else:
    print('O Computador ganhou')
    print(f'Numero escolhido: {num}')
