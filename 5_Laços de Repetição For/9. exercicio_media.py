import os 
os.system("clear")


media = 0
for i in range(4):
   nota = float(input(f"Digite a {i+1}ª nota: "))
   media += nota

print(f"MÉDIA: {media/4}")


print("\nFIM DO PROGRAMA")