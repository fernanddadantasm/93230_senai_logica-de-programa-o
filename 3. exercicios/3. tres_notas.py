#LIMPAR O TERMINAL.
import os
os.system("clear")

#ELABORE UM ALGORITMO PARA SOLICITAR AO USUÁRIO TRÊS NOTAS.
#CALCULE A MÉDIA DO ALUNO SEJA MENOR QUE 7, O ALUNO ESTÁ REPROVADO.
#CASO A MÉDIA DO ALUNO SEJA MENOR QUE 7, O ALUNO ESTÁ REPROVADO.
#MOSTRAR: MÉDIA E SE ESTÁ APROVADO



#SOLICITANDO DADOS
primeira_nota = float(input("Digite a primeira nota: "))
segunda_nota = float(input("Digite a segunda nota: "))
terceira_nota = float(input("Digite a terceira nota: "))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma / 3 

print(f"Média: {media}")

if media < 7:
    print("REPROVADO!")
else:
    print("APROVADO!")    



