'''
idoso = True
gestante = False
pessoa_deficiencia = False
pessoa_crianca_colo = False


if idoso and pessoa_deficiencia and gestante and pessoa_crianca_colo:
    atendimento_preferencial = True

if idoso or pessoa_deficiencia or gestante or pessoa_crianca_colo:
    atendimento_preferencial = True

if (idoso and pessoa_deficiencia) or (gestante and pessoa_crianca_colo):
    atendimento_preferencial = True

if (idoso or pessoa_deficiencia) and (gestante or pessoa_crianca_colo):
    atendimento_preferencial = True
'''

'''
idoso = True
gestante = False
pessoa_deficiencia = True
pessoa_crianca_colo = False

preferencia = 0


if pessoa_deficiencia:
    print('Com deficiência')
    preferencia = 5
if idoso:
    pr
    preferencia = 4

if pessoa_crianca_colo:
    preferencia = 3

if gestante:
    preferencia = 2
'''

def tratar_senha(senha_sem_tratar):
    senha_tratada = senha_sem_tratar
    if senha_sem_tratar % 2 == 0:
        senha_sem_tratar = 'p' + str(senha_tratada)
    else:
        senha_tratada = 'I' + str(senha_tratada)
    return senha_tratada

    print(f'A senha é: {senha_tratada}')
    return senha_tratada

# função com parâmetro de entrada e com retorno
def mostrar_senha_com_retorno(senha_sem_tratar):
    senha_tratada = tratar_senha(senha_sem_tratar)
    return senha_tratada

# função com parâmenta de entrada e sem retorno
def pedir_senha():
    senha = int(input('Informe uma senha: '))
    return senha

# função sem parâmetro de entrada e com retorno
def mostrar_mensagem():
    print('Essa é uma mensagem qualuquer. ')

senha_sem_tratar = pedir_senha()
trocar_senha(senha_sem_tratar)
teste1 = mostrar_senha_com_retorno(teste2)
mostrar_mensagem()