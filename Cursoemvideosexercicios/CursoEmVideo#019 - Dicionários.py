'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f' O {pessoas["nome"]} tem {pessoas["idade"]} anos.')'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.values())'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(pessoas.items())'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
pessoas['peso'] = 98.5
for k, v in pessoas.items():
    print(f'{k} = {v}')'''

'''brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[0]['uf'])
print(brasil[1]['uf'])'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')'''

'''estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('sigla do Estado: '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(v, end='')
    print()'''