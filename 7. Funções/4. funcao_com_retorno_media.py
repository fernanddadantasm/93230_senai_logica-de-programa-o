import os
os.system("clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma / 2
    return media

primeiro_numero = int(input("Digite o primeiro número: "))
segunda_numero = int(input("Digite o segundo número: "))

media = calcular_media(primeiro_numero , segunda_numero)

print(f"Média: {media}")