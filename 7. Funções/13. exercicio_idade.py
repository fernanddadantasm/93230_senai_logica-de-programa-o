import os 
os.system ("clear") 

#Escreva um programa que solicite ao usuário o ano de
#nascimento e, utilizando uma função, retorne com a idade do usuário.

ano_nascimento = int(input("Digite seu ano de nascimento: "))

def idade(ano_nascimento):
    idade_nascimento = 2025 - ano_nascimento 
    return idade_nascimento

idade_nascimento = idade(ano_nascimento)

print(f"Sua idade é: {idade_nascimento}")
