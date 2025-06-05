import os 
os.system("clear")

login_cadastrado = "fernanda.dantas@hotmail.com"
senha_cadastrada = "123456"
contador = 1 


for i in range(3):
  
    login = input("Login: ")
    senha = input("Senha: ")
    
    if login_cadastrado == login and senha_cadastrada == senha:
        print("Acesso permitido")
        break

      
    else:
        print("Acesso negado")
        if i == 2:
           print("Número de tentativas execidido")
          





    