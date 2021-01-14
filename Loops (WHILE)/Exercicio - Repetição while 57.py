sexo = input('Por gentileza, digite seu sexo: ').strip().lower()[0]
while sexo not in 'MmFf':
    sexo = input('Sexo inválido, por gentileza, digite novamente: ')
print('Cadastro com sucesso')
if sexo in 'Mm':
    print('Seu sexo é masculino')
else:
    print('Seu sexo é feminino')

