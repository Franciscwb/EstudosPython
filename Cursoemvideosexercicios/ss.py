salarioMinimo = 1000

def calculaNovoSalario(salarioBruto, descontoPlanoSaude, descontosDiversos):
    salarioLiquido = salarioBruto
    salarioLiquido -= descontosDiversos
    salarioLiquido -= descontoPlanoSaude * (50 / 100)
    salarioLiquido += salarioMinimo * (8 / 100)
    salarioLiquido += salarioBruto * (5 / 100)

    return salarioLiquido

calculaNovoSalario(1500, 500, 300)