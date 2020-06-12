from datetime import datetime

nascimento = int(input('Qual o seu ano de NASCIMENTO: '))

idade = 2020 - nascimento


print('O seu ano de nascimento é: '.format(nascimento))
print('Idade aproximada: '.format(idade))