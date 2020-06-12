#ETAPA 01
print('=' * 55)

import time
time.sleep(0)

print('Esta é a \033[1;30mLoja Saint Grail.\033[m')
import time
time.sleep(0)

print('Seja \033[1;30mBem-Vindo(a)\033[m!')
import time
time.sleep(0)

print('Aqui quem fala é o vendedor \033[1;30mFrancis de  Almeida\033[m')
import time
time.sleep(0)

print('Faremos uma análise de crédito.')
import time
time.sleep(0)

print('Para tal, digite os seguintes dados Por favor.')
import time
time.sleep(0)


print('=' * 55)
import time
time.sleep(0)

cargo_empresa = str(input('Qual o seu \033[1;30mCARGO NA EMPREGA\033[m que trabalha atualmente: '))
import time
time.sleep(0)

salario = float(input('Digite o seu \033[1;30msalário atualmente:\033[m '))
import time
time.sleep(0)

ano_nascimento = int(input('Digite o seu \033[1;30mano de nascimento\033[m? '))
import time
time.sleep(0)



#ETAPA 02
    #Análise de crédito

from datetime import date
hj = date.today()
idade = hj.year

limiteGasto = salario * (idade / salario) + 100
import time
time.sleep(0)

print('=' * 55)
print('\033[1;30mMuito Obrigado\033[m pelas informações. \nconforme o que foi preenchido seus dados são estes a seguir ')
print('O seu salário atual é: \033[1;30mR${:.2f}\033[m '.format(salario))
print('A sua idade aproximada é: \033[1;30m{} anos\033[m'.format(idade-ano_nascimento))
print('Você tem um limite de gasto de: \033[1;30mR${:.2f}\033[m '.format(limiteGasto))
print('=' * 55)
time.sleep(0)
#ETAPA 03
    #Quantidade de caracteres

primeiro_nome = 'Francis'
nome_completo = 'Francis de Almeida'
(len(primeiro_nome))

#Digitar o nome de um produto
time.sleep(0)
produto = str(input(f'Digite o \033[1;30mNOME\033[m de um \033[1;30mPRODUTO:\033[m '))

#Digitar o valor de um produto
time.sleep(0)
valor_p = float(input('Digite o \033[1;30mVALOR DO PRODUTO:\033[m '))


'''
Valor do produto menor ou igual 60% do limite de gasto print liberado
Valor do produto entre 60% e 90% do limite de gasto print liberado ao parcelar em até 2 vezes.
Valor do produtro entre 90% e 100% do limite print liberado ao parcelar em 3 ou mais vezes
caso contrário BLOQUEADO
'''

if valor_p <= (limiteGasto * 60 / 100):
    print('=' * 55)
    print('\033[1;30mLiberado!\033[m')
    print('=' * 55)

elif valor_p >= (limiteGasto * 60 / 100):
    print('=' * 55)
    print('liberado ao parcelar em até 2 vezes.')
    print('=' * 55)

elif valor_p >= (limiteGasto * 90 / 100):
    print('=' * 55)
    print('Liberado ao parcelar em 3 ou mais vezes.')
    print('=' * 55)

elif valor_p >= (limiteGasto):
    print('=' * 55)
    print('Bloqueado.')
    print('=' * 55)


#Se o produto estiver entre a quantidade de caracteres do nome completo e a idade do cliente
#terá um desconto igual à quantidade de caracteres do seu primeiro nome
#Mostrar o valor do produto com desconto

print('Valor do produto: \033[1;30mR${:.2f}\033[m'.format(valor_p))