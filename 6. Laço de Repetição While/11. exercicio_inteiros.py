import os
os.system("clear")

contador = 0
soma = 0
par = 0
impar = 0
soma_pares = 0
soma_geral = 0
while True:
    numero = int(input("Digite um número: ")) 
    if numero == 0 :
        break
    if numero % 2 == 0:
        par += 1
        soma_pares += numero
    if numero % 2 == 1:
        impar += 1
    
    contador += 1
    soma_geral += numero
media_pares = soma_pares / par
media_geral = soma_geral / contador


print(f"Quantidade de números pares: {par}")    
print(f"Quantidade de números impares: {impar}")
print(f"Média de valores pares: {media_pares}")
print(f"Média geral: {media_geral}")





     
   
        

        
      
     

    

