import os
os.system("clear")

soma = 0
preco = 0
while True:
    opcao = int(input("""
Código \t Prato \t\t\t Valor
1 \t Picanha \t\t R$25,00
2 \t Lasanha \t\t R$20,00
3 \t Strogonoff \t\t R$18,00                                    
4 \t Bife Acebolado \t R$15.00
5 \t Pão com ovo \t\t R$5,00
                  
Digite a opção desejada:                   
"""))
    match opcao:
     case 1:
        print("Picanha")
        preco = 25
     case 2:
        print("Lasanha")
        preco = 20
     case 3:
        print("Strogonoff")
        preco = 18
     case 4:
        print("Bife Acebolado")
        preco = 15
     case 5:
        print("Pão com ovo")
        preco = 5
     case _:
        print("Opção inválida!")
        preco = 0
    soma += preco     
    resposta = input("Deseja escolher outro prato? s/n ")
           

    if resposta == "n":
       break



print(f"\nTotal a pagar: R${soma:.2f}")




        



         