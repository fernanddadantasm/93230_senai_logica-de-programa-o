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
   
        

        
      
     

    

