import os 
os.system("clear")

while True:
    
    nota = float(input("Digite uma nota: "))
    
    if nota < 0 or nota > 10:
        print(input("Digite uma nota: "))
    else:
        break

print(f"Nota: {nota}")
  