num = int(input('Digite um numero entre 1 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u} \nDezena: {d} \nCentena: {c} \nMilhar: {m}')

#num = int(input('Digite um numero entre 0 e 9999: '))
#if num < 0 or num > 9999:
#    print('Numero fora de opções')
#elif num > -1 and num < 10:
#    num1 = str(num)
#    print(f'Unidade: {num1[0]} \nDezena: 0 \nCentena: 0 \nMilhar: 0')
#elif num > 9 and num < 100:
#    num1 = str(num)
#    print(f'Unidade: {num1[1]} \nDezena: {num1[0]} \nCentena: 0 \nMilhar: 0')
#elif num > 99 and num < 1000:
#    num1 = str(num)
#    print(f'Unidade: {num1[2]} \nDezena: {num1[1]} \nCentena: {num1[0]} \nMilhar: 0')
#else:
#    num1 = str(num)
#    print(f'Unidade: {num1[3]} \nDezena: {num1[2]} \nCentena: {num1[1]} \nMilhar: {num1[0]}')
