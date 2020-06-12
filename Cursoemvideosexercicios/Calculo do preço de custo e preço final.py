#Na prática, introdução à lógica de programação e ambiente Python
#Programa de auxílio ao cálculo do preço de custo e preço final

#v_couro é o valor do couro para fabricação unitária
v_couro = float(input("Digíte o valor do COURO: "))

#v_solado é o valor para fabricação unitária
v_solado = float(input("Digite o valor do SOLADO: "))

#v_cordões é o valor de cordões e ilhoses para fabricação unitária
v_cordoes = float(input("Digite o valor de CORDÕES E ILHOSES: "))

#v_insumos é o valor dos insumos diversos para fabricação unitária
v_insumos = float(input("Digite o valor de INSUMOS: "))

#v_mão de obra é o valor de mão de obra para fabricação unitária
v_mao_de_obra = float(input("Digite o VALOR DE MÃO DE OBRA: "))

#v_marketing é o valor de Marketing e Propaganda dividido pela produção
v_marketing = float(input("Digite o valor de MARKETING: "))

#v_vendas é o valor do custo de vendas dividido pela produção
v_vendas = float(input("Digite o valor dos custos de VENDAS: "))

#CÁLCULO DO PREÇO DE CUSTO
preço_custo = (v_couro * 0.30) + (v_solado * 0.20) + (v_cordoes * 0.05) + (v_insumos * 0.05) + (v_mao_de_obra * 0.20) + (v_marketing * 0.10) + (v_vendas * 0.10)
print("O preço de custo unitário deste modelo de sapato é R${:.2f}".format(preço_custo))

#CALCULANDO O PREÇO FINAL:
#CALCULO DO PREÇO ADICIONANDO LUCRO DO FABRICANTE
preço_lucro = preço_custo * 1.30

#CALCULO DO PREÇO ADICIONANDO PERDAS DE CAPITAL
preço_perdas = preço_lucro * 1.15

#CALCULO DO PREÇO ADICIONANDO IMPOSTOS FEDERAIS
preço_IPI_CONFINS = preço_perdas * 1.15

#CALCULO DO PREÇO ADICIONANDO MARGEM DE VENDAS
preço_vendas = preço_IPI_CONFINS * 1.25

#CALCULO DO PREÇO ADICIONANDO IMPOSTOS ESTADUAIS E MUNICIPAIS
preço_ICMS_INSS = preço_vendas * 1.30

#PREÇO FINAL, ACRESCIDO DE TODOS OS IMPOSTOS E MARGENS DE LUCRO
preço_final = preço_ICMS_INSS
print("O preço final ao consumidor deste modelo de sapato é R${:.2f} ".format(preço_final))