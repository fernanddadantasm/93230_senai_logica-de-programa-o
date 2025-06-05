import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Dados:
    nome: str
    idade: int
    peso: float
    altura: float

dados1 = Dados("Maria Antônia", 25, 63.3, 1.67 )

print("===DADOS===")
print(f"\nNome: {dados1.nome} \nIdade: {dados1.idade} \nPeso: {dados1.peso} \nAltura: {dados1.altura}")
