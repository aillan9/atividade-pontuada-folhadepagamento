import os

os.system ("cls || clear")


def calcular_inss(salario_base):
        if salario_base <= 1100.00:
                return salario_base * 0.075
        elif salario_base <= 2203.48:
                return salario_base * 0.09
        elif salario_base <= 3305.22:
                return salario_base * 0.12
        elif salario_base <= 6433.57:
                return salario_base * 0.14
        return 854.36

def calcular_irrf(salario_base, dependentes=1):
        base_irrf = salario_base - (dependentes * 189.59)
        if base_irrf <= 2259.20:
                return 0.0
        elif base_irrf <= 2826.65:
                return base_irrf * 0.075
        elif base_irrf <= 3751.05:
                return base_irrf * 0.15
        elif base_irrf <= 4664.68:
                return base_irrf * 0.225
        return base_irrf * 0.275

def calcular_folha_pagamento():
        salario_base = float(input("Salário base (R$): "))
        optou_vt = input("Deseja vale transporte? (s/n): ").lower() == 's'
        valor_vr = float(input("Valor do vale refeição (R$): "))

        inss = calcular_inss(salario_base)
        irrf = calcular_irrf(salario_base)
        vt = salario_base * 0.06 if optou_vt else 0.0
        vr = valor_vr * 0.20
        plano_saude = 150.00

        salario_liquido = salario_base - (inss + irrf + vt + vr + plano_saude)

        print(f"Salário Líquido: R$ {salario_liquido:.2f}")



calcular_folha_pagamento()