import os
os.system("clear")

numero = int(input("Digite um número: "))
def par_impar (numero):
    par_impar = numero
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"
resultado = par_impar(numero)      
print(f"O número digitado é {resultado}")   

    