import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    email: str
    telefone: str
    endereco: str
    def exibindo_dados(self):
        print("\n===Exibindo dados===")
        print(f"\nNome: {self.nome} \nemail: {self.email} \ntelefone: {self.telefone} \nendereco: {self.endereco}")



print("===SOLICITANDO DADOS===")
nome = input("Digite seu nome: ")
email = input("Digite seu email: ")
telefone = input("Digite seu telefone:  ")
endereco = input("Digite seu endereço: ")

dados1 = Dados(nome, email, telefone, endereco)
dados1.exibindo_dados()