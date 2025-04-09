import os 
os.system("clear")
#.
#Escreva um programa que solicite ao utilizador o fornecimento do seu peso em kg 
#e de sua altura em m e a partir deles calcule o índice de massa corpórea do utilizador.

peso = float(input("Digite o seu peso em KG: "))
altura = float(input("Digite a sua altura em M: "))

def peso_altura_ideal(peso, altura):
    calculo_peso_e_altura = peso / (altura ** 2) 
    return calculo_peso_e_altura
def clasificacoes_imc(calculo_peso_e_altura):
    if calculo_peso_e_altura < 18.5:
        return "Abaixo do peso, consulte um nutricionista."
    elif 18.5 <= calculo_peso_e_altura <= 24.9: 
        return "Peso normal, mantenha hábitos saudáveis."
    elif 25 <= calculo_peso_e_altura <= 29.9: 
        return "Sobrepeso, considere uma dieta balanceada e atividade física."
    elif 30 <= calculo_peso_e_altura <= 34.9:  
        return "Obesidade Grau 1, procure orientação de um profissional de saúde."
    elif 35 <= calculo_peso_e_altura <= 39.9:
        return "Obesidade Grau 2, consulte um médico para avaliação e orientação."
    elif calculo_peso_e_altura >= 40: 
        return "Obesidade Grau 3, busque assistência médica imediatamente."
    else:
        "Erro! Calcule novamente o IMC"
calculo_peso_e_altura = peso_altura_ideal(peso, altura)
recomendacao_imc = clasificacoes_imc(calculo_peso_e_altura)
print(f"Seu IMC é: {calculo_peso_e_altura:.2f}")
print(f"{recomendacao_imc}")

