# Manipulando Strings

#Fatiando
frase = 'Curso em vídeo python'
print(frase[0])

#Utilizar 3 aspas faz o python imprimir o texto conforme digitado no código

#Contar caracteres
compr = len(frase)
print(compr)

#Contar quantas vezes aparece
vezes = frase.count('o')
print(vezes)

#Achar um pedaço de string
onde = frase.find('deo')
print(onde)

#Perguntar se existe uma parte especifica dentro da string (Letras maisculas são diferentes de minusculas
tem = 'Curso' in frase
print(tem)

#substituir parte de string
novafrase = frase.replace('python', 'Android')
print(novafrase)

# Transformação de textos

#Deixar tudo maiscula
maiscula = frase.upper()
print(maiscula)

#Deixar tudo minuscula
minuscula = frase.lower()
print(minuscula)

#Deixar primeira letra de palavras
pletra = frase.title()
print(pletra)

#Deixar primeira letra da string
pstring = frase.capitalize()
print(pstring)

#remover espaços inuteis (Apenas no inicio e final) *Também pode escolher o lado com R ou L
ex1 = '    Curso em python              '
remove = ex1.strip()
print(remove)

#dividir uma string em uma lista
ex2 = 'Curso em video'
divid = ex2.split()
print(divid)

#Juntar uma lista em uma string
junto = '-'.join(divid)
print(junto)