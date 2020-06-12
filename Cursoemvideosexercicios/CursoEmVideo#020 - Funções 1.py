#Exemplo sem melhoramento.
'''a = 4
b = 5
s = a + b
print(s)

a = 8
b = 9
s = a + b
print(s)

a = 2
b = 1
s = a + b
print(s)'''


'''def soma(a, b):
    s = a+ b
    print(s)
    #necessita de duas linhas de espaço para o def reconhecer.


#Programa Principal
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(4, 1)'''

'''def soma(a, b):
    s = a+ b
    print(s)
    #necessita de duas linhas de espaço para o def reconhecer.


#Programa Principal
soma(a = 4, b = 5)'''

'''def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
    #necessita de duas linhas de espaço para o def reconhecer.


#Programa Principal
soma(a = 4, b = 5)'''

'''def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)'''

'''def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)'''