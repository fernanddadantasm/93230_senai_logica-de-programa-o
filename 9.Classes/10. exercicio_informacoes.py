import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    idade: int
    peso: float
    altura:float
    def exibir_dados(self):
         print(f"Nome: {self.nome} \nIdade: {self.idade} \nPeso: {self.peso} \nAltura: {self.altura}\n")

pessoas_dados = []
QUANTIDADE_PESSOAS = 4

for i in range(QUANTIDADE_PESSOAS):
    pessoas = Dados(
                    nome=input("Digite seu nome: "),
                    idade=int(input("Digite sua idade: ")),
                    peso=float(input("Digite seu peso: ")),
                    altura=float(input("Digite sua altura: "))
                    )
    pessoas_dados.append(pessoas)
    os.system("clear")



os.system("clear")
print("===DADOS===")
for pessoas in pessoas_dados:
    pessoas.exibir_dados()


