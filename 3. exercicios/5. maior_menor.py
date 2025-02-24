#LIMPAR O TERMINAL.
import os
os.system("clear")

# Elabore um algoritmo usando operações lógicas para solicitar ao usúario 2 números e escrever:
# Os 2 números informados 
# O maior número
# O menor número

primeiro_numero = int(input("Digite um número: "))
segundo_numero = int(input("Digite o segundo número: "))

menor = min(primeiro_numero, segundo_numero)
maior = max(primeiro_numero, segundo_numero)

print("\nExibindo resultados: ")
print(f"Primeiro número: {primeiro_numero}")
print(f"Segundo número: {segundo_numero}")
if primeiro_numero == segundo_numero:
    print("Os números são iguais.")
else:
    print(f"Primeiro número: {primeiro_numero}")
    print(f"Segundo número: {segundo_numero}")
    print(f"MENOR: {menor}")
    print(f"MAIOR: {maior}")









