


print('Esta é a Loja Saint Grail.\nSeja Bem-Vindo! \nAqui quem fala é o vendedor Francis de Almeida')

print('Faremos uma análise de crédito.\nPara tal, digite o seguintes dados')

cargo_empresa = str(input('Qual o seu CARGO NA EMPREGA que trabalha atualmente: '))

salario = float(input('Digite o seu salário atualmente: '))

anoNascimento = int(input('Qual sua data de nascimento? '))


from datetime import date
hj = date.today()
idade = hj.year

limiteGasto = salario * (idade / salario) + 100

print('Muito Obrigado pelas informações. \nconforme o que foi preenchido seus dados são estes a seguir ')
print('O seu salário atual é: R${:.2f} '.format(salario))
print('Idade aproximada é: {}'.format(idade-anoNascimento))
print('Você tem um limite de gasto de: R${} '.format(limiteGasto))

produto = str(input(f'Digite o NOME de um PRODUTO: '))
valor_p = float(input('Digite o VALOR DO PRODUTO: '))


print('O nome do produto é: {} '.format(produto))
print('O valor do produto é: R${:.2f} '.format(valor_p))

'''
Valor do produto menor ou igual 60% do limite de gasto print liberado
Valor do produto entre 60% e 90% do limite de gasto print liberado ao parcelar em até 2 vezes.
Valor do produtro entre 90% e 100% do limite print liberado ao parcelar em 3 ou mais vezes
caso contrário BLOQUEADO
'''

if valor_p <= (limiteGasto * 60 / 100):
    print('Liberado!')
elif valor_p >= (limiteGasto * 60 / 100):
    print('liberado ao parcelar em até 2 vezes.')
elif valor_p >= (limiteGasto * 90 / 100):
    print('Liberado ao parcelar em 3 ou mais vezes.')
elif valor_p >= (limiteGasto):
    print('Bloqueado.')

'''
Se o valor do produto estiver entre a quantidade de caracteres do seu nome completo e a idade do cliente,
mostrar que ele terá um desconto igual À quantidade de caracteres do seu primeiro nome
'''


'''
if valor_p <= (limiteGasto * 60 / 100):
    print('Liberado!')
if valor_p >= (limiteGasto * 60 / 100):
    print('liberado ao parcelar em até 2 vezes')
if valor_p >= (limiteGasto * 90 / 100):
    print('Liberado ao parcelar em 3 ou mais vezes')
if valor_p >= (limiteGasto):
    print('Bloqueado')
'''



