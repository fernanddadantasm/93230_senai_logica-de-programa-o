import os 
os.system ("clear")

#Fazer um programa que solicita o preço de um produto e
#inflaciona esse preço em 10% se ele for menor que 100 e
#em 20% se ele for maior ou igual a 100. 
#Utilize uma função com retorno para obter o resultado solicitado.

preco = float(input("Digite o valor do produto: "))


def inflacao(preco):
    if preco >= 100:
        preco_inflacao = preco * 1.20
    elif preco < 100:
        preco_inflacao = preco * 1.10
    return preco_inflacao

def desconto(preco):
    if preco >= 100:
        preco_desconto = preco * 0.10
        return preco_desconto
    elif preco < 100:
        preco_desconto = preco * 0.20
        return preco_desconto 

preco_inflacao = inflacao(preco)
preco_desconto = desconto(preco)
print(f"O valor do produto com a inflação é: {preco_inflacao:.2f}")
print(f"O valor do produto com desconto é: {preco_desconto:.2f}")