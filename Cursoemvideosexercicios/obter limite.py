'''
print('Esta é a Loja Saint Grail.')
print('Seja Bem-Vindo!')
print('Aqui quem fala é o vendedor Francis de Almeida')
print('Faremos uma análise de crédito.Para tal, digite o seguintes dados')
'''

from datetime import date
data_de_hoje = date.today


def linha():
    print('=' * 30)




def obter_limite():


    if obter_limite:

        linha()
        cargo_atual = str('Analista')
        salario_atual = int(1000)
        ano_nascimento = int(1984)
        data_de_hoje = (data_de_hoje - ano_nascimento)

        limite_gasto = (salario_atual * (idade_aproximada / 1000) + 100)

        linha()

        print('Cargo: {}'.format(cargo_atual))
        print('Salário: {}'.format(salario_atual))
        print('Ano de nascimento: {}'.format(ano_nascimento))
        print('Idade aproximada: {}'.format(ano_nascimento - data_de_hoje))



        linha()



obter_limite()







'''
    print('Muito Obrigado pelas informações. \nconforme o que foi preenchido seus dados são estes a seguir ')
    print('O seu salário atual é: R${:.2f} '.format(salario))
    print('Idade aproximada é: {}'.format(idade - anoNascimento))
    print('Você tem um limite de gasto de: R${} '.format(limiteGasto))
'''
