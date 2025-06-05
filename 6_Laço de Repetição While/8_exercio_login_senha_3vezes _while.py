import os 
os.system("clear")
#fer

login_cadastrado = "fernanda.dantas@hotmail.com"
senha_cadastrada = "123456"
contador = 0 


while True:
  
    login = input("Login: ")
    senha = input("Senha: ")
    
    if login_cadastrado == login and senha_cadastrada == senha:
        print("Acesso permitido")
        break

      
    else:
        print("Acesso negado")
        contador += 1
        
    if contador == 3:
           print("Número de tentativas execidido")
           break


          





    