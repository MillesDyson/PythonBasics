frase = 'a torre da derrota'
junto = ''.join(frase.split())
print(junto)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto:
    print('palindromo')
else:
    print('não palindromo')

