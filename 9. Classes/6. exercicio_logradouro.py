import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Endereço: 
    logradouro: str
    numero: str
@dataclass
class Pessoa: 
    nome: str
    idade: int
    endereco: Endereço
    
    def exibir_dados(self):
        print(f"\nNome: {self.nome} \nIdade: {self.idade} \nLogradouro: {self.endereco.logradouro} \nNúmero: {self.endereco.numero}")

endereco1 = Endereço("Rua A", "33")        
pessoa1 = Pessoa("Marta", 22, endereco1)
            
print("===Dados de pessoas===")
pessoa1.exibir_dados()