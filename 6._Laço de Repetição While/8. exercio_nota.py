import os 

os.system("clear")


contador = 0 
nota = 0
while True:
    contador += 1
    nota += float(input("Digite uma nota: "))
    resposta = input("Deseja inserir mais uma nota? S/N ").upper()
    if resposta == "N":
        print(f"Média: {nota/contador}")
        break    
    
#Evita dvisão por zero
    #if contador == 0:
    #   soma = nota
    #   contador = 1

