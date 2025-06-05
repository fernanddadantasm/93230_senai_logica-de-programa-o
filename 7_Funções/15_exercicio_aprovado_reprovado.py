import os 
os.system("clear")

#Escreva um programa que permita ler 2 notas de um aluno e informe
#por meio de funções:
#A média;
#Com base na média, se o aluno está aprovado ou reprovado.
#Critério para aprovação: média 7,0.

nota = 0
QUANTIDADE_NOTA = (2)

for i in range(QUANTIDADE_NOTA):
    nota += float(input("Digite uma nota: "))
    def media(nota):
        nota_media = nota / 2
        return nota_media
    def aprovado_reprovado(nota_media):
        if nota_media >= 7:
            return "Aprovado, parabéns!"
        else: 
            return "Reprovado, estude mais!"


nota_media = media(nota)
resultado_aprovado_reprovado = aprovado_reprovado(nota_media)

print(f"Sua média é: {nota_media}")
print(f"{resultado_aprovado_reprovado}")