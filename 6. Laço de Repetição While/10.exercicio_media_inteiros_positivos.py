#Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. 
#O final da leitura acontecerá quando for lido um valor negativo.
#Mostre a média aritmética dos números informados pelo usuário.


import os
os.system("clear")

contador = 0
soma = 0
numero = 0
while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    else:
        contador += 1 
        soma += numero


media = soma / contador
print(f"Média {media}")        
   
        

        
      
     

    

