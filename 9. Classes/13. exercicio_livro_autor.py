import os 
os.system("clear")

from dataclasses import dataclass

@dataclass
class Autor: 
    nome:str 
    biografia:str
@dataclass
class Livro:
    titulo:str
    ano: int
    autor: Autor
    def exibir_dados(self):
        print(f"\nNome do autor: {self.autor.nome} \nTitulo do livro: {self.titulo} \nAno de publicação: {self.ano}")

autor1 = Livro(
              titulo= input("Digite o titulo do livro: "),
              ano= int(input("Digite o ano de publicaçao: ")),
              autor=Autor(
                    nome= input("Digite o nome do autor: "),
                    biografia= input("Digite a biografia do autor: ")
                )
            )
with open("livros.txt", "a") as arquivo_livro:
    arquivo_livro.write(f"{autor1.autor.nome}, {autor1.titulo}, {autor1.ano}\n")
print("DADOS SALVOS COM SUCESSO")
os.system("clear")
print("===DADOS===")
autor1.exibir_dados()