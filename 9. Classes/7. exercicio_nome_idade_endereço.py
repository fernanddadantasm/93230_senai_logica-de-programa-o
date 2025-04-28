import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Endereço: 
    logradouro: str
    numero: str
    cidade: str 

@dataclass
class Pessoa: 
    nome: str
    email: str
    endereco: Endereço

    def exibir_dados(self):
        print(f"\nNome: {self.nome} \nEmail: {self.email}\nLogradouro: {self.endereco.logradouro} \nNúmero: {self.endereco.numero} \nCidade: {self.endereco.cidade}")


nome = input("Digite seu nome:  ")
email = input("Digite seu email: ")
logradouro = input("Digite o logradouro: ")
numero = input("Digite o número: ")
cidade = input("Digite a cidade: ")
endereco = Endereço(logradouro, numero, cidade)
dados1 = Pessoa(nome, email, endereco)

os.system("clear")
print("=== Dados de pessoas ===")
dados1.exibir_dados()