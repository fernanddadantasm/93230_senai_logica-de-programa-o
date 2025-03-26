import os 
os.system("clear")
idade = 0
quantidade_mulheres = 0 




while True:
    print("""
Código | Descrição 
1 \t Adicionar Pessoa
2 \t Exibir Resultado
3 \t Sair
""")
    opcao = int(input("Digite a opção desejada: "))                   
    
    match opcao:
        case 1:
            idade = int(input("Digite sua idade: "))
            genero = (input("""                 
M - Masculino
F - Femnino
Digite seu gênero:                    
""")).upper()
            salario = float(input("Digite o valor do seu sálario: "))
            if genero == "F" and salario >= 5.000:
                quantidade_mulheres += 1


          
            
          
                
            
                
            
                
                




