'''nota01 = input('Digite a primeira nota: ')
nota02 = input('Digite a segunda nota: ')
nota03 = input('Digite a terceira nota: ')'''

'''#Exemplo de sintaxe do comando while com incremento de variável:
cont = 1 #inicialização da variável contadora
while cont<=3:
    #mensagem repetida enquando a condição (cont<=3) for verdadeira
    print(str(cont) +'a execução do laço')
    cont+=1 #incremento da variável contadora
    
                    1a execução do laço
                    2a execução do laço
                    3a execução do laço'''



'''Exemplo da sintaxe do comando while com decremento de variável:
cont = 5 #inicialização da variável contadora
while cont>=1:
    #mensagem repetida enquanto a condição (cont>=1) for verdadeira
    print ('Imprimindo',(5-cont+1),'mensagem')
    cont-=1 #Decremento da variável contadora
    
    
            Imprimindo 1 mensagem
            Imprimindo 2 mensagem
            Imprimindo 3 mensagem
            Imprimindo 4 mensagem
            Imprimindo 5 mensagem'''


'''#Exemplo da sintaxe do comando while com o comando break
cont = 1 #Inicialização da variável contadora
while True:
    #Mensagem a ser repetida até que o comando break,
    #Dentro do bloco do if seja executado
    print (str(cont)+'a execução do while!')
    cont+=1  #Incremento da variável contadora
    #Verifica se a variável contadora é maior do que 3
    if (cont>3):
        break
#Instrução imediatamente após o laço
print('Execução do while acabou')

            1a execução do while!
            2a execução do while!
            3a execução do while!
            Execução do while acabou'''


'''#Exemplo while e continue
cont = 1 #Inicialização da variável contadora
while cont<10:
    cont+=1 #Incremento da variável contadora
    #teste condicional se o número é ímpar
    if(cont%2==1):
        continue    #Salta para a próxima execução do loop
print(cont)     #Print somente quando cont é par
    
            2
            4
            6
            8
            10'''

'''#Exemplo sequência de Fibonacci
controle = 1    #Variável de controle da repetição
#Laço de controle do menu interativo
while controle == 1:
    num = int(input('Digite quantos elementos você quer imprimir: '))
    a, b = 0, 1
    cont = 2    #Variável contadora
    print('Sequência de Fibonacci')
    print(a, b, end="") #Imprime os dois primeiros valores
    #Laço de repetição para calcular a sequência
    while cont<num:
        a, b = b, a+b   #Atualiza os valores da sequência
        print(b, end=" ")   #Imprime valor atual da sequência
        cont+=1 #Incremeta a variável contadora
    print() #Quebra de linha
    #Menu interativo para repetir o cálculo da sequência
    controle = int(input('Digite 1 para continuar ou 0 para parar: '))'''

'''#Exemplo calculadora simples
controle = 1
while True:
    print('Mini calculadora')
    print('1-Somar dois números')
    print('2-Subtrair dois números')
    print('3-Multiplicar dois números')
    print('4-Dividir dois números')
    print('5-Fatorial de um número')
    print('6-Potência entre dois números')
    print('7-Sair')
    controle = int(input('Escolha uma opção: '))
    if (controle == 7):
        break
    print('----------------------------', end='\n')
    #Teste das opções
    if controle ==1:
        num_01 = float(input('Digite um número: '))
        num_02 = float(input('Digite outro número: '))
        print('\nA soma de', num_01, 'e', num_02, 'é', num_01+num_02)
        print('----------------------------------------', end='\n')

    elif controle == 2:
        num_01 = float(input('Digite um número: '))
        num_02 = float(input('Digite outro número: '))
        print('\nA subtração de',num_01, 'e', num_02, 'é', num_01-num_02)
        print('---------------------------------------', end='\n')
    elif controle == 3:
        num_01 = float(input('Digite um número: '))
        num_02 = float(input('Digite outro número: '))
        print('\nA multiplicação de',num_01, 'e',num_02,'é',num_01*num_02)
        print('---------------------------------------', end='\n')
    elif controle == 4:
        num_01 = float(input('Digite um número: '))
        num_02 = float(input('Digite outro número: '))
        if num_02 == 0:
            print('Não é possível fazer divisão por zero')
            print('------------------------------------', end='\n')
        else:
            print('\nA divisão de',num_01, 'e', num_02, 'é', num_01/num_02)
            print('------------------------------------', end='\n')
    elif controle == 5:
        num_01 = float(input('Digite um número: '))
        fatorial = 1
        contador = num_01
        while contador>1:
            fatorial *= contador
            contador -= 1
        print('\nO fatorial de',num_01, 'é', fatorial)
        print('----------------------------------', end='\n')
    elif controle == 6:
        num_01 = float(input('Digite um número: '))
        num_02 = float(input('Digite outro número: '))
        print('\n', num_01, 'elevado a', num_02, 'é', num_01**num_02)
        print('-----------------------------------', end='\n')

print('----------------------------------------', end='\n')
print('Fim da calculadora')'''


'''#while-else
cont = 1
while cont<=3:
    print('Bloco while() e condicao == True')
    cont+=1
else:
    print('Bloco Else e condicao == else')'''