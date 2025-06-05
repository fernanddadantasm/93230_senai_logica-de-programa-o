import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Informacôes_livros:
    nome: str
    autor: str
    categoria: str
    preco: float
    def exibir_dados(self):
        print(f"Nome: {self.nome} \nIAutor: {self.autor} \nCategoria: {self.categoria} \nPreço: {self.preco}\n")

livros_quantidade = []
LIVROS = 3

for i in range(LIVROS):
    livros = Informacôes_livros(
                                nome=input("Digite o nome do livro: "),
                                autor=input("Digite o nome do autor: "),         
                                categoria= input("Digite a categoria: "),
                                preco= input("Digite o preço: ")
                                )
    livros_quantidade.append(livros)
    os.system("clear")

nome_arquivo = ("Dados_livros,txt")
with open(nome_arquivo, "a") as livros_adquiridos: 
    for livros in livros_quantidade:
        livros_adquiridos.write(f"{livros.nome}, {livros.autor}, {livros.categoria}, {livros.preco}\n")
print("DADOS SALVOS COM SUCESSO")
os.system("clear")
print("===Dados dos livros===")

for livros in livros_quantidade:
    livros.exibir_dados()
