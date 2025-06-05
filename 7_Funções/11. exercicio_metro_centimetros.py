import os 
os.system("clear")

numero = float(input("Digite um valor em metros: "))

def metros_centimetros(numero):
    conversao = numero * 100
    return conversao
    #return centimetros * 100;

conversao_centimetros = metros_centimetros(numero)
#conversao_centimetros = metros_centimetros(numero)

print(f"O valor digitado tem {conversao_centimetros:.0f} centímetros")

 


    
         
