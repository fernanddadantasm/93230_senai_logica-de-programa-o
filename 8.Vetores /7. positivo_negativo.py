import os 
os.system("clear")
#Crie um algoritmo que preencha um vetor com 5 números, 
# Mostre a quantidade de números negativos e a soma dos números positivos desse vetor.


QUANTIDADE_NUMEROS = 5
lista_positivo = []
lista_negativo = []

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
        lista_negativo.append(numero)
    else:
        lista_positivo.append(numero)

soma_positivo = sum(lista_positivo)
quantidade_negativo = len(lista_negativo)
print(f"A quantidade de números negativos é: {quantidade_negativo}")
print(f"A soma dos números positivos é: {soma_positivo}")
