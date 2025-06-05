#LIMPAR O TERMINAL.
import os
os.system("clear")

#Elabore um algoritmo para solicitar dois números e ao final mostre na tela:
#A média, a soma, o produto, o menor valor e o maior valor.
#Usando uma linha para cada resultado.

primeiro_numero = int(input("Digite o primeiro número: "))
segundo_numero = int(input("Digite o segundo número: "))

# media = (primeiro_numero + segundo_numero) / 2

soma = primeiro_numero + segundo_numero
media = soma / 2
produto = primeiro_numero * segundo_numero

if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = segundo_numero
    maior = primeiro_numero    


print("\nExibindo resultados: ")
print(f"SOMA: {soma}")
print(f"MÉDIA: {media}")
print(f"PRODUTO: {produto}")
print(f"MENOR: {menor}")
print(f"MAIOR: {maior}")





