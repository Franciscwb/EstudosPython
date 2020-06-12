'''num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 5')
#num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')'''

'''valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista.')'''

'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}"')
print(('Cheguei ao final da lista.'))'''

'''#Peculiaridade do PYTHON em listas
#ligação em lista
a = [2, 3, 4, 7]
b = a
b[2] = 8 #O Python cria uma lisgação entre uma lista e a outra.
print(f'Lista A: {a}')
print(f'Lista b: {b}')

a = [2, 3, 4, 7]
b = a[:]  #Tipo fatiamento, não fará uma ligação mas sim uma cópia entre A e B.
b[2] = 8 #O Python cria agora uma cópia entre as listas.
print(f'Lista A: {a}')
print(f'Lista b: {b}')'''