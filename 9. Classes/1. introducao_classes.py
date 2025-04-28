import os 
os.system("cls || clear")
from dataclasses import dataclass
@dataclass
class Pessoa:
    nome:str
    idade: int

@dataclass 
class Pet:
    nome: str 
    idade: int
    raca: str

pessoa1 = Pessoa("Marta ", 30)
pessoa2 = Pessoa("José ", 40 )

pet1 = Pet("Toto", 4, "Pastor-alemão")
pet2 = Pet("Hulk", 6, "Pitbull")

print("DADOS DAS PESSOAS: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade} ")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade} ")

print("DADOS DOS PETS: ")
print(f"Nome: {pet1.nome}, idade: {pet1.nome}, Raça: {pet1.raca}")
print(f"Nome: {pet2.nome}, idade: {pet2.nome}, Raca: {pet2.raca} ") 