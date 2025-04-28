import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    idade: int
    peso: float
    altura: float

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

dados1 = Dados(nome=nome, idade=idade, peso=peso, altura=altura)
#dados1 = Dados(nome, idade, peso, altura)

print("=== DADOS COLETADOS ===")
print(f"\nNome: {dados1.nome} \nIdade: {dados1.idade} \nPeso: {dados1.peso} \nAltura: {dados1.altura}")