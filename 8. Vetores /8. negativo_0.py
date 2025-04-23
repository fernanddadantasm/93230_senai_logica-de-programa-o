import os 
os.system("clear")
#Crie um algoritmo que receba do usuário valores e armazene em um vetor 5 números, 
#caso seja informado um valor negativo, atribua o valor 0.
#Liste os valores do vetor.


lista = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º número: "))
    if numero < 0:
       numero = 0 
    lista.append(numero)

print(f"VALORES NO VETOR: {lista}")
