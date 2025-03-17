import os 
os.system("clear")

numero = int(input("Digite um número para tabuada: "))

for i in range(1, 11): # range(11) esse é outra forma de utilizar, colocando o número inteiro
                       #o laço comeca a partir do zero e vai até o número escolhido;
    print(f"{numero} X {i} = {numero * i} ")
print("FIM DO PROGRAMA") 
    