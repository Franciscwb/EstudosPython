'''
def tabuada(n):  #def apenas define uma função
    for c in range(1, 11):
        print('{} x {} = {}'.format(n, c, n * c))

n = int(input('informe N: '))

#Chamada a função
tabuada(n)
tabuada(2)
tabuada(6)
tabuada(8)
'''



'''
def dividir_times(inscritos):

    time1 = []
    time2 = []

    for c in range(6):

        #Se for par
        if c % 2 == 0:
            time1.append(inscritos[0])
        else:
            time2.append(inscritos[c])
    return time1, time2



#Aqui acaba a função

inscritos = ()

for c in range(6):
    nome = input('Nome do jogador {}: '.format(c))
    inscritos.append(nome)

print('=========inscritos========')
for nome in inscritos:
    print('---')


time1, time2 = dividir_times(inscritos)

print('----TIME 1 ----')
for nome in time1:
    print('-',nome)

print('----TIME 2 ----')
for nome in time2:
    print('-',nome)
'''

'''
def sacar(saldo):
    montante = float(input('Quanto deseja sacar? '))
    saldo = saldo - montante
    return saldo


saldo = float(input('Informe o saldo total: '))
qtde = int(input('Quantos saques você deseja? '))

for c in range(qtde):
    saldo = sacar(saldo)

print('Saldo final: ',saldo)
'''


inicio = 1987
fim = 2020

ano = int(input('Informe um ano: '))

if ano >= 1987 and ano <= 2020:
    print('Este ano está no meu intervalo de nascimento')
else:
    print('Não!')
