nome = str(input('\033[1;30mQual é o seu nome:\033[1;30m '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jessica Juliana':
    print('belo nome feminino')
else:
    print('Seu nome é bem normal.')
print('\033[1;30mTenha um bom dia, {}!\033[m'.format(nome))