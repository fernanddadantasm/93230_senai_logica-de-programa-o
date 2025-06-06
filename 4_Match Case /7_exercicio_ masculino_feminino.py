import os 
os.system("clear")

#Entrada
altura = float(input("Digite sua altura: "))
genero = str(input(""" 

M - Masculino
F - Femnino

Digite seu gênero:                    

""")).upper()
# O comomando . depois de uma variável declarada abre um menu com opçoes
# a opçao ".upper() serve para formatar, quando você digita uma opçaõ minuscula
# mas na declaração do case ela está maiscula, esse comando vai fazer a formação dela
# para o formato certo e não cair no case de "Opção inválida"

#Processamento
match  genero:
    case "M":
        peso_ideal = (72.7 * altura) - 58
        print(f"Seu peso ideal é: {peso_ideal:.2f}")
        
    case "F":
        peso_ideal = (62.1 * altura) - 44.7
        print(f"Seu peso ideal é: {peso_ideal:.2f} ")
    case _:
        print("Opção inválida")
        

#Saída