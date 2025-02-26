import os
os.system("clear")

#Elabore um algortimo usando operações lógicas para informar se uma pessoa é obrigada a votar. 
#Considere que a regra é que menores de 18 e maiores que 65 não são obrigados a votar. 

idade = int(input ("Digite sua idade: "))

if idade < 18 or idade > 65:
    print("NÃO É OBRIGADO A VOTAR!")
else:
    print("É OBRIGADO A VOTAR!")    



