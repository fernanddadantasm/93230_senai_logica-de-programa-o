import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    email: str
    telefone: str
    endereco: str

dados1 = Dados("Maria Antônia", "maria.antonia@gmail.com", "(71) 9 9960-2450", "Rua das Hortênsias, Nº20" )

print("===DADOS===")
print(f"\nNome: {dados1.nome} \nemail: {dados1.email} \ntelefone: {dados1.telefone} \nendereco: {dados1.endereco}")
