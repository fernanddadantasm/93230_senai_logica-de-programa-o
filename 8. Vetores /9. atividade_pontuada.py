def calcular_irrf(salario, dependentes):
    # Dedução por dependente
    deducao_por_dependente = 189.59
    salario_base = salario - (dependentes * deducao_por_dependente)

    if salario_base <= 2112.00:
        aliquota = 0
        desconto = 0
    elif salario_base <= 2826.65:
        aliquota = 7.5 / 100
        desconto = salario_base * aliquota
    elif salario_base <= 3544.00:
        aliquota = 15 / 100
        desconto = salario_base * aliquota
    elif salario_base <= 4256.00:
        aliquota = 22.5 / 100
        desconto = salario_base * aliquota
    else:
        aliquota = 27.5 / 100
        desconto = salario_base * aliquota

    return desconto


# Exemplo de uso
salario = float(input("Digite o salário do funcionário: "))
dependentes = int(input("Digite a quantidade de dependentes: "))

irrf = calcular_irrf(salario, dependentes)
print(f"O desconto do IRRF é: R$ {irrf:.2f}")