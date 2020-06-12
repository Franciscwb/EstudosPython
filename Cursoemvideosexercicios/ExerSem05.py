'''#a
N = int(input('Entre com o valor de N: '))
i = 0
while i<=N:
    print(i)
    i = i+1'''
from typing import List

'''#b
N = int(input('Entre com o valor de N: '))
while i <= N:
    print(i)
    i = i+1'''

'''#c
N = int(input('Entre com o valor de N: '))
i = 0
while i <= N:
    print (i)'''

'''#d
N = int(input('Entre com o valor de N: '))
i = 0
while i <= N: i++
print(i)'''

'''#e
N = int(input('Entre com o valor de N: '))
i =0
while i i++
    print(i)'''

'''#produtório
N = int(input('Escreva o valor de N: '))
produtorio = 1
i = 1
while i <= N:
    produtorio = produtorio * i
    i = i + 1
    print('O produtório de', N, 'é', produtorio)'''

'''#Gradiente descendente

def gradiente_descendente(x0, função, gradiente):
    precisao = 1
    taxa_aprendizagem = 0.0001
    max_intercacoes = 1000
    x_novo = x0
    f_x_novo = função(x_novo)
    f_x_velho = função(x_novo) + 100
    i = 0

    while (abs(f_x_novo - f_x_velho) > precisao) and (i <= max_intercacoes):
        f_x_velho = x_novo
        x_novo = x_velho - taxa_aprendizagem * gradiente(x_velho)
        f_x_novo = função(x_novo)
        fxVelho = função(x_velho)
        i = i + 1

    print('Precisão alcançada: ',(f_x_novo - f_x_velho))
    print('x=', x_novo)
    print('f(x) =',f_x_novo)
    return[x_novo, f_x_novo]'''

'''lista = [10, 11, 12, 13, 14, 15]
for valor in lista:
    print(valor)'''

'''texto = 'PYTHON'
for caracter in texto:
    print(caracter)'''

'''#No function
dados = [[1, 2, 3],[4,5,6],[7,8,9]]

soma = 0
qtde = 0


for valor in dados:
    soma += valor
    qtde += 1

print(soma)
print(qtde)

media = soma / qtde

print(media)'''

'''soma = 0

for numero in range(10):
    if (numero % 2) == 0:
        soma += numero'''

'''varA = 3
varB = 0
for num in range(varA):
    varB += num ** 2'''


'''for fruta in lista:
for letras in fruta:
qtdeLetras += 1
print(fruta, qtdeLetras)'''


'''for fruta in lista: 
for letras in fruta: 
qtdeLetras += letras 
print(fruta, qtdeLetras)'''


'''for fruta in lista: 
qtdeLetras = 0 
for letras in fruta: 
    qtdeLetras += letras 
    print(fruta, qtdeLetras)'''


for fruta in lista:
    qtdeLetras = 0
for letras in fruta: 
    qtdeLetras += 1
    print(fruta, qtdeLetras)


'''for fruta in lista:
qtdeLetras = 0 
for letras in fruta: 
qtdeLetras *= 1 
print(fruta, qtdeLetras)'''