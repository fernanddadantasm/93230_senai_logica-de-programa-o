import os
os.system("clear || cls")

#limpando o terminal em windows ou Linux

#Entrada
matricula = input("Digite o seu número de matrícula: ")
ano_nascimento = int(input("Digite o ano de seu nascimento: "))
tempo_trabalho = int(input("Digite quantos anos você trabalhou: "))

#processemento 
idade = 2025 - ano_nascimento


if idade >= 65 or tempo_trabalho >= 30:
    resultado = "Requerer aposentadoria"

else:
    resultado = "Não requrer aposentdoria"

    


print(f"MATRÍCULA: {matricula}")
print(f"Idade: {idade}")
print(f"Tempo de trabalho: {tempo_trabalho}")
print(f"Resultado: {resultado}")






      
