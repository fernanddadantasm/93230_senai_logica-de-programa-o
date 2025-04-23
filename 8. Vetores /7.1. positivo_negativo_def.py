import os 
os.system("clear")
#Crie um algoritmo que preencha um vetor com 5 números, 
# Mostre a quantidade de números negativos e a soma dos números positivos desse vetor.


QUANTIDADE_NUMEROS = 5
lista_positivo = []
negativo = 0

def soma_positivo(lista):
    soma = 0
    for numero in lista:
        if numero > 0:
            soma += numero
    return soma


for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
        negativo += 1
    else:
        lista_positivo.append(numero)

soma = soma_positivo(lista_positivo)


print(f"A quantitade de números negativos é: {negativo}")
print(f"A soma dos números positivos é: {soma}")

