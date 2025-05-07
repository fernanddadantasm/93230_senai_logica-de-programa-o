import os 
os.system("clear")
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome:str
    data_admissao: str
    matricula:str
    endereco: str
    def exibir_dados_funcionario(self):
        print(f"\nNome: {self.nome} \nData de Admissão: {self.data_admissao} \nMatícula: {self.matricula} \nEndereço: {self.endereco}")   
@dataclass
class Cliente:
    nome:str
    data_nascimento: str
    endereco: str
    def exibir_dados_cliente(self):
        print(f"\nNome: {self.nome} \nData de Nascimento: {self.data_nascimento} \nEndereço: {self.endereco}")
QUANTIDADE_PESSOA = 3
opcao = input("\n1 - Funcionário \n2 - Cliente \nDigite a opção de cadastro desejada : ")
os.system("clear")
match opcao:
    case "1": 
        informacoes_funcionario = []
        for i in range(QUANTIDADE_PESSOA):
            funcionario = Funcionario(nome= input("Digite seu nome: "),
                                     data_admissao= input("Digite a sua data de admissão: "),
                                     matricula= input("Digite sua matrícula: "),
                                     endereco= input("Digite seu endereço: ")
                                    ) 
            informacoes_funcionario.append(funcionario)
            os.system("clear")
            arquivo_nome = ("Informacoes_funcionarios.txt")
        with open (arquivo_nome, "a") as funcionarios_informacoes:
            for funcionarios in informacoes_funcionario:
                funcionarios_informacoes.write(f"\n{funcionarios.nome} \n{funcionarios.data_admissao} \n{funcionarios.matricula} \n{funcionarios.endereco}\n ")
        print("DADOS SALVOS COM SUCESSO")
        os.system("clear")
    case "2": 
        informacoes_clientes = []
        for i in range(QUANTIDADE_PESSOA):
            cliente = Cliente(nome= input("Digite seu nome: "),
                              data_nascimento= input("Digite sua data de nascimento: "),
                              endereco= input("Digite seu endereço: ")     
                             )
            informacoes_clientes.append(cliente)
        arquivo_nome = ("Informacoes_clientes.txt")
        with open (arquivo_nome, "a") as clientes_informacoes:
            for clientes in informacoes_clientes:
                clientes_informacoes.write(f"\n{clientes.nome} \n{cliente.data_nascimento} \n{cliente.endereco} \n")
        print("DADOS SALVOS COM SUCESSO")
        os.system("clear")
    case _:
        print("Opção Inválida")
        os.system("clear")
   