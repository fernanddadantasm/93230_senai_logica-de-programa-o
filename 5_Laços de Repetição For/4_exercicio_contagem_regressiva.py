import os 
import time
os.system("clear")

numero = int(input("Digite um número: "))

for i in range(numero, 0, -1):
    print(f"CONTAGEM REGRESSIVA: {i}")
    time.sleep(1)
print("FIM DO PROGRAMA")    