import os
os.system("clear")

#Entrada
nome = (input("Digite seu nome: "))
primeira_nota = float(input("Digite  a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))

#Processamento
media = (primeira_nota + segunda_nota) / 2

if media >= 9:
    conceito = "A"
elif media > 7.5:
    conceito = "B"
elif media >= 6:
    conceito = "C"
elif media >= 4:
    conceito = "D"
else:
    conceito = "E"
match conceito:
    case "A" | "B" | "C":
        print(f"Conceito: {conceito}")
        print("Aprovado")
    case  "D" | "E":
        print(f"Conceito: {conceito}")
        print("REPROVADO")
    case _:
        print("Opção inválida.")








           
