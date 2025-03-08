import os
os.system("clear")

# Entrada
valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 - À vista
2 - A prazo
Digite a forma de pagamento:                               
"""))

# Processamento
match forma_de_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        valor_final = valor_produto - desconto
        print(f"""
Valor do produto: R$ {valor_produto:.2f}
Forma de pagamento: À vista
Valor do desconto: R$ {desconto:.2f}
Total a pagar: R$ {valor_final:.2f}
""")

    case 2:
        num_parcelas = int(input("""
1x
2x
3x
4x
5x
6x
Digite o número de parcelas: 
"""))
        valor_parcela = valor_produto / num_parcelas
        print(f"""
Valor do produto: R$ {valor_produto:.2f}
Forma de pagamento: A prazo
Quantidade de parcelas: {num_parcelas}
Valor por parcela: R$ {valor_parcela:.2f}
Total a prazo: R$ {valor_produto:.2f}
""")

    case _:
        print("Opção inválida")
        


#Saída
 



       
        



        




