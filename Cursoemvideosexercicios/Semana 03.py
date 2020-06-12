'''texto = "alterando o valor de sep"
print(texto)
print('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', sep=' --- ')

#pula uma linha
print()

texto = "Alterando o valor de sep e end"
print(texto)
print('Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4', sep=' --- ', end='...\n')'''

'''raio = 3
pi = 3.1415
area = pi * raio
print('Raio do círculo: ',raio, 'cm')
print('Área do círculo: ',area, 'cm^2')'''

''''print ('\n\nOlá, prezado aluno!.\nTudo bem?\tVamos Aprender Python')'''

'''print('\nMês\tDias\nJan\t31\nFev\t28\nMar\t31\nAbr\t30\n ...')'''

'''x = input('Entre com seu nome: ')
print('Olá, ' + x + ', tudo bem?')'''

'''nome = input('Digite o seu nome: ')
sobrenome = input('Digite o seu sobrenome: ')
print('Olá ' + nome + ' ' + sobrenome + '\nBem Vindo!')'''

'''#input() e print() com casting
#Solicita nome, idade e altura ao usuário
nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura (m): '))
#imprime os dados no console
print('Olá ' + nome + '\n')
print('Sua idade é: ' + str(idade) + ' anos.\n')
print('Sua altura é: ' + str(altura) + ' metros.')'''

''''#conversão de temperaturas
#comando input solicita o usuário a digitar uma temperatura
#Método float faz uso da casting da string para um valor numérico
temp_c = float(input('Digite a temperatura em graus celsius: '))

temp_f = 1.8 * temp_c + 32  #Converte de Celsius para Fahrenheit
temp_k = temp_c + 273.15    #Converte de Celsius para Kelvin

#Imprime o resultado no console
print('Temperatura em Celsius: ' + str(temp_c))
print('Temperatura em Fahrenheit: ' + str(temp_f))
print('Temperatura em Kelvin: ' + str(temp_k))'''

''''#utilizando format()
#Mensagem a ser impressa
mensagem = 'Valor decimal: {0}\nValor Hexadecimal: {1}'

print('Programa para converter de decimal para hexa')
print()

num_dec = int(input('Digite um número: '))
print()

num_hex = format(num_dec, 'x')
print()

print(mensagem.format(num_dec, num_hex))'''

''''#Método eval() formatando valores numéricos
#Programa para calcular real para dólar
print()
print('Programa para calcular real para dólar')
print()

real = float(input('Digite um valor em reais: '))
print()

dolar = float(input('Digite o valor do dólar atual (em reais): '))
print()

valor_convert = real / dolar
print('R$ {0:.2f} valem: U$ {1:.2f}'.format(real, valor_convert))'''

'''#Utilização eval()
#Solicita uma equação
equacao = input('Escreva uma equação: ')
#Interpreta o texto como comando
x = eval(input('Escreva o valor de x:'))

#imprime o resultado no console
print(equacao + '=' ,eval(equacao),'se x = {0}'.format (x))'''

'''#Exemplo strftime
from datetime import datetime

hoje = datetime.now()   #Lê a data e tempo atual

#Imprime as informações separadas
ano = hoje.strftime('%Y')
print('Ano: ', ano)

mes = hoje.strftime('%m')
print('Mês: ', mes)

dia = hoje.strftime('%d')
print('Dia: ',dia)'''

'''print('Dia\tMês\tAno\n01\t01\t2019')'''

'''entrada = input('Digite um número: ')
saida = entrada * 3
print('Saída:',saida)'''

'''nome = input('Nome: ')
altura = float(input('Altura(m): '))
massa = float(input('massa(Kg): '))

imc = massa / (altura * altura)

print('Nome\tAltura\tMassa\tIMC\n{}\t{}\t{}\t{:.2f}'.format(nome, altura, massa, imc))'''

'''from datetime import  datetime

usuario = input('login: ')

hora = datetime.now() .time()
print('Usuário {usuario} logou às {H}:{M}:{S}'.format(usuario = usuario, H = hora.hour, M = hora.minute, S = hora.second))'''

'''def calculadora():
    num1 = float(input('Digite um número:'))
    num2 = float(input('Digite outro número:'))
    operação = input('Digite a operação desejada (+, -, *, /):')

    resultado = num1

    if operação == '+':
        resultado += num2
    elif operação == '-':
        resultado -= num2
    elif operação == '*':
        resultado *= num2
    elif operação == '/':
        resultado /= num2
    else:
        print('Operação não reconhecida. Tente de novo!')

    print('O resultado é %f' % resultado)

calculadora()'''


'''a = input('Digite sua nota: ')
nota = float (a)

if nota >=7.0:
    print('Você está APROVADO por média.')
elif nota>9.0:
    print('Parabéns!')
    print('Boas Férias!')
elif nota>=4:
    print('Você pode fazer R2.')
    print('Venha na próxima semana')
else:
    print('Você está reprovado!')
    print('Você não pode fazer R2.')

print('Acabou.')'''



