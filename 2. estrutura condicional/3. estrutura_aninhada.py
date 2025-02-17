import os
os.system("clear")

idade = 10

if idade < 12:
    print("Acesso negado.")
elif idade < 18:
    print("Somente com permisão dos pais!")    
else:
    print("Acesso permitido.")   


print("==FIM!==")