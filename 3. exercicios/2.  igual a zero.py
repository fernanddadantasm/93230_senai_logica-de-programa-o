#LIMPAR O TERMINAL.
import os
os.system("clear")

# Elabore um algoritmo para solicitar ao usuário um valor e 
# escrever a mensagem: É MAIOR QUE 10!
# Se o valor lido for maior que 10, caso contrário escrever:
#NÃO É MAIOR QUE 10!
#Verifique se o número digitado é igual a 10, caso seja, escreva a mensagem: "O número é igual a 10!"


#SOLICITANDO DADOS 
valor = int(input("Digite um número: "))
print(f"Valor: {valor}")

#Estrutura condicional

if valor < 10:
    print("NÃO É MAIOR QUE 10!")
elif valor == 10:
    print("O número é igual a 10!")
else:
    print("É MAIOR QUE 10!")



