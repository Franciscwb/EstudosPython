#DESAFIO DE GERENCIAMENTO DE RH

nome_funcionario = str(input('Insira o nome do FUNCIONÁRIO: '))

endereço_funcionario = str(input('Insira o ENDEREÇO do funcionário: '))

data_admissao = str(input('Insira a DATA DE ADMISSÃO: '))

area_atuacao = str(input('Insira a ÁREA DE ATUAÇÃO: '))

carga_horaria_diaria = float(input('insira a CARGA HORÁRIA DIÁRIA: '))

carga_horaria_semanal = (carga_horaria_diaria * 5)

valor_pago_hora_aula = float(input('Insira o VALOR PAGO POR HORA AULA: '))

custo_semanal = (valor_pago_hora_aula * carga_horaria_diaria * 5)

custo_mensal = (custo_semanal * 4)


print('Nome do funcionário: {} '.format(nome_funcionario))
print('Endereço do funcionário: {} '.format(endereço_funcionario))
print('Data de admissão {} '.format(data_admissao))
print('Área de Atuação: {} '.format(area_atuacao))
print('Carga horária diária {:.0f}hs '.format(carga_horaria_diaria))
print('Carga horária semanal {:.0f}hs '.format(carga_horaria_semanal))
print('Valor pago por hora aula: R${:.2f} '.format(valor_pago_hora_aula))
print('Valor semanal: R${:.2f} '.format(custo_semanal))
print('Custo mensal: R${:.2f} '.format(custo_mensal))