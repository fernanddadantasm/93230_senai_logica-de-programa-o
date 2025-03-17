import os
os.system("clear")
soma = 0
for i in range(5):
   nota = int(input(f"Digite a {i+1}ª nota: "))
   soma = soma + nota
   #soma += nota A variável soma nesse caso está fazendo a soma com ela mesma;
   # e depois ela faz a soma com a outra vaviável de nome nota
print()
print(f"Soma: {soma}")

print("FIM DO PROGRAMA")   
