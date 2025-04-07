import os 
os.system("clear")

#Faça uma função sem retorno com nome: logo_senai()
#Limpado o terminal e inserindo: ==== SENAI DENDEZEIROS ===

#Solicite ao usuário dois números 
#Cada um em uma variácvel diferente 
#Crie uma função com retorno para somar os dois números informados pelo usuário

def logo_senai():
    os.system("clear")
    print("=== SENAI DENDEZEIROS ===")

def calcular_soma(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    return soma
def calcular_subtracao(primeira_nota, segunda_nota):
    subtracao = primeira_nota - segunda_nota
    return subtracao
def calcular_multiplicacao(primeira_nota, segunda_nota):
    multiplicacao = primeira_nota * segunda_nota
    return multiplicacao
def calcular_divisao(primeira_nota, segunda_nota):
    divisao = primeira_nota / segunda_nota #// serve para pedir o resto da divisão
    return divisao
   
logo_senai()
primeiro_numero = int(input("\n""Digite o primeiro número: "))
logo_senai()
segundo_numero = int(input("\nDigite o segundo número: "))

soma = calcular_soma(primeiro_numero, segundo_numero)
subtracao = calcular_subtracao(primeiro_numero, segundo_numero)
multiplicacao = calcular_multiplicacao(primeiro_numero, segundo_numero)
divisao = calcular_divisao(primeiro_numero, segundo_numero)

logo_senai()
print(f"Soma: {soma}")
print(f"\nSubtração: {subtracao}")
print(f"\nMultiplicção: {multiplicacao}")
print(f"\nDivisão: {divisao:.2f}")





