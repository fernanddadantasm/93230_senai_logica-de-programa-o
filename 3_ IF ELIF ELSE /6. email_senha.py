import os
os.system("clear")
#.

#Elabore um algortimo


usuário_cadastrado = "fernanda.dantas@hotmail.com"
senha_cadastrada = "231068"

login = str(input ("Login: "))
senha = str(input( "Senha: "))



if login == usuário_cadastrado and senha == senha_cadastrada:
    print("Bem vindo")
else:
    print("Login ou senha inválidos!")
