import os 
os.system("clear")

numero = int(input("Digite um número: "))

def positivo_negativo (numero):
    positivo_negativo = numero
    if numero > 0:
        print("Esse número é positivo")
    if numero < 0:
        print("Esse número é negativo")    
    if numero == 0:
        print("Zero é um número neutro")


resultado = positivo_negativo(numero)     