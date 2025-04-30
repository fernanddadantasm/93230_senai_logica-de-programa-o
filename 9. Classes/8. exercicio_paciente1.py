import os 
os.system("clear")
from dataclasses import dataclass
#Atributos são variaveis que pertecem a classe
@dataclass
class Paciente:
    nome: str
    idade: int
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n\n")

#paciente1 = Paciente(nome="Marta", idade=45)
paciente1 = Paciente(
                    nome=input("Digite o nome do paciente: "),
                    idade=int(input("Digite a idade do paciente: "))
                    )
os.system("clear")
print("Dados do Paciente")
paciente1.exibir_dados()
