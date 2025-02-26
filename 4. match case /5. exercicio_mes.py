import os
os.system("clear")

#Escreva um programa utilizando o comando match-case
#que mostre um mês do ano de acordo com o número digitado pelo usuário


#Entrada 
mes_ano = int(input("Digite um número para um mês do ano: "))


#Processamento
match mes_ano:
    case 1: 
        print("January")
    case 2: 
        print("February")
    case 3: 
        print("March")
    case 4: 
        print("April")
    case 5: 
        print("May")
    case 6: 
        print("June")
    case 7:
        print("July")
    case 8: 
        print("Agust")
    case 9: 
        print("September")
    case 10: 
        print("October")
    case 11: 
        print("November")
    case 12: 
        print("December")
    case _: 
        print("Opção inválida")


#Saída
 



       
        



        




