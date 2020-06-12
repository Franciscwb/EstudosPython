# 1 Mostrar nome completo junto com nome da loja
print('=' * 50)
print('Você digitou os seguintes dados')
print('Seu cargo é: Analista')
print('Seu salário é: R$1000.00')
print('Seu ano de nascimento é: 1984')
print('=' * 50)


ano_nascimento = int(1984)

from datetime import date
data_hoje = date.today()
idade = data_hoje.year

limite_gasto = 1000 * (idade / 1000) + 100


print('A sua idade aproximada é: {}anos'.format(idade-ano_nascimento))
print('Valor disponível LIMITE DE GASTO R${:.2F} '.format(limite_gasto))

print('Produto: Bicicleta')
valor_produto=int(50)
print('O valor do Produto é: R${:.2f}'.format(valor_produto))

if valor_produto <= (limite_gasto * 60 / 100):
    print('Liberado')

elif valor_produto <= (limite_gasto * 60 / 100) or  (valor_produto <= (limite_gasto * 90 / 100)):
    print('Liberado até 2 vezes')

elif valor_produto <= (limite_gasto * 90 / 100) or (valor_produto <= (limite_gasto)):
    print('Liberado até 3 vezes')

elif valor_produto < (limite_gasto * 10):
    print('"BLOQUEADO')


# Obter desconto através dos caracteres do nome completo idade com relação ao primeiro nome

caracteres_nome = int('18'.format(int))

desconto = int(valor_produto - 7)

if valor_produto <= (18):
    print('Recebera desconto')
if valor_produto <= (36):
    print('Recebra desconto')
    print('O valor do produto de R${:.2f} com desconto ficou R${:.2f} '.format(valor_produto,desconto))








