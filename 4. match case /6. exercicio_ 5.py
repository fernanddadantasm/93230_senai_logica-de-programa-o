import os
os.system("clear")

#Entrada 
valor_produto = float(input("Digite o valor do produto: "))
forma_de_pagamento = int(input("""
1 - A vista
2 - A prazo
Digite a forma de pagamento:                               
                                                                                    
"""))


#Processamento
match forma_de_pagamento:
    case 1:
        desconto = valor_produto * 0.10
        print()
    case 2:
        input("""
1x
2x
3x
4x
5x
6x
Digite o número de parcelas: 
""")    
    case _:
        print("Opção invalida")

        
        


#Saída
 



       
        



        




