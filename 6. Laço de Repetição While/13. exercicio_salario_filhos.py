
#A prefeitura de uma cidade fez uma pesquisa entre seus habitantes,
#coletando dados sobre o salário e número de filhos das famílias da cidade.A prefeitura deseja saber:
#a) total de famílias que responderam a pesquisa;
#b) média do salário da população;
#c) média do número de filhos;
#d) maior salário;
#e) menor salário.
#Crie um menu com duas opções.
#Código |   Descrição
#   1       Adicionar família
#   2       Sair e exibir resultados
#O final da leitura de dados se dará com quando o usuário digitar o número código 2. 




import os 
os.system("clear")

salario = 0
soma_salarios = 0
total_familias = 0 
numero_filhos = 0 
filhos = 0
maior_salario = 0
menor_salario = 0

while True:
    print("""
Código | Descrição 
1 \t Adicionar Pessoa
2 \t Sair e Exibir Resultado

""")
    opcao = int(input("Digite a opção desejada: "))  
    match opcao:
        case 1:
            salario = float(input("Digite o valor do seu sálario: "))
            filhos = int(input("Digite a quantidade de filhos: ")) 
            total_familias += 1
            soma_salarios += salario
            numero_filhos += filhos
        case 2:     
            print(f"\nExibindo resultados")
            print(f"Total de familias: {total_familias}")
            print(f"Média de salários: R$ {soma_salarios / total_familias:.3f}")
            print(f"Média de filhos: {numero_filhos / total_familias}")
            print(f"Maior salário: {maior_salario}")
            print(f"Menor salário: {menor_salario}")
            print(f"\nPrograma encerrado")
            break



#Falta só colocar o maior e menor salário
 
    