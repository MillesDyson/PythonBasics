import random
print("""JOKENPO!
Escolha sua opção:
[1] PEDRA
[2] PAPEL
[3] TESOURA
Pedra Papel ou tesoura?: """, end='')
player = int(input('').strip().lower())
joken = ['0', 'Pedra', 'Papel', 'Tesoura']
escolhido = random.randint(1, 3)

if 0 < player < 4:
    print('-='*15)
    print(f'O computador escolheu {joken[escolhido]}')
    print(f'O jogador escolheu {joken[player]}')
    print('-='*15)

    if escolhido == 2 and player == 1 \
            or escolhido == 3 and player == 2 \
            or escolhido == 1 and player == 3:
        print('Computador ganhou!')
    elif escolhido == 1 and player == 2 \
            or escolhido == 2 and player == 3 \
            or escolhido == 3 and player == 1:
        print('Jogador ganhou!')
    else:
        print('Empate!')
else:
    print('Opção Incorreta!!')
