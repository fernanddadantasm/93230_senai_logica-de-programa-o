import os 
os.system("clear")

login_cadastrado = "fernanda.dantas@hotmail.com"
senha_cadastrada = "123456"

while True:
    login = input("Login: ")
    senha = input("Senha: ")
    if login_cadastrado == login and senha_cadastrada == senha:
      print("Acesso permitido")
      break

    else:
        print("Acesso negado")





    