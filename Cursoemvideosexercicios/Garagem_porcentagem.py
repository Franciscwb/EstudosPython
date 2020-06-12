Largura_Garagem = float(input("Entre com a largura da garagem em metros: "))
Profundidade_Garagem = float(input("Entre com a profundidade da garagem em metros: "))

# Abaixo, cálculo da área da garagem
Area_Garagem = Largura_Garagem * Profundidade_Garagem

Largura_Terreno = float(input("Entre com a largura do terreno em metros: "))
Profundidade_Terreno = float(input("Entre com a profundidade do terreno em metros: "))

# Abaixo, cálculo da área do terreno
Area_Terreno = Largura_Terreno * Profundidade_Terreno

# Agora, cálculo do percentual de ocupação
Percentual = ((Area_Garagem) / (Area_Terreno)) * 100
print("Percentual de ocupação:",Percentual)

# Entrada da zona de localização do terreno
zona = input('Entre com Zona de Localização: Sul=S, Norte=N e Oeste=W : ')

#relatórios e mensagens
print('Imóvel localizado na zona: ',zona)
print('Percentual de ocupação: ',Percentual)

if zona == 'N' and Percentual <= 25:
    print('Projeto atende norma de zoneamento do plano diretor')
elif zona == 'L' or zona == 'W' and Percentual <= 30:
    print('Projeto atende norma de zoneamento do plano diretor')
elif zona == 'S' and Percentual <= 40:
    print('Projeto atende norma de zoneamento do plano diretor')

else:
    print('REVISAR MEDIDAS. Projeto NÃO atende norma de zoneamento do plano diretor')

