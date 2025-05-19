import os 
os.system("clear")
from dataclasses import dataclass
#Atributos são variaveis que pertecem a classe
@dataclass
class Paciente:
    nome: str
    idade: int
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIdade: {self.idade}\n")

paciente_lista = []
QUANTIDADE_PACIENTE = 2
#paciente1 = Paciente(nome="Marta", idade=45)
for i in range(QUANTIDADE_PACIENTE):
    paciente = Paciente(
                    nome=input("Digite o nome do paciente: "),
                    idade=int(input("Digite a idade do paciente: "))
                    )
    paciente_lista.append(paciente) 

nome_arquivo = ("Dados_paciente,txt")
with open(nome_arquivo, "a") as arquivos_pacientes: 
#w serve para quando você precisa substituir os dados que estão no arquivo já criado, 
#a serve para acumular dados nesse arquivo
    for paciente in paciente_lista:
        arquivos_pacientes.write(f"{paciente.nome}, {paciente.idade}\n")
print("DADOS SALVOS COM SUCESSO")
os.system("clear")
print("===Dados dos Pacientes===")
for paciente in paciente_lista:
    paciente.exibir_dados()
