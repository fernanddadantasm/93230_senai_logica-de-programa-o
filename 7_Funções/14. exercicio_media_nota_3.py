import os 
os.system("clear")

#Escreva um programa que permita ler 3 notas de
#um aluno, usando laço de repetição e informe por meio de uma função a média;
nota = 0
QUANTIDADE_NOTA = (3)

for i in range(QUANTIDADE_NOTA):
    nota += float(input("Digite uma nota: "))
    def media(nota):
        nota_media = nota / 3
        return nota_media

nota_media = media(nota)
print(f"Sua média é: {nota_media}")


    



