import os
from unittest import case
os.system("clear")


dia = input("Digite dia da semana: ")

match dia: 
    case "Segunda":
        print("Hoje é segunda - feira.")

    case "Terça":
        print("Hoje é terça - feira.")

    case "Quarta":
        print("Hoje é Quarta - feira.")

    case "Quinta":
        print("Hoje é Quinta - feira.")
    case "Sexta":
        print("Hoje é Sexta - feira.")

    case "Sábado" | "Domingo":
        print("Hoje é final de semana")

    case _:
        print("Dia inválido.")

print(dia)

print("===FIM===")

        




