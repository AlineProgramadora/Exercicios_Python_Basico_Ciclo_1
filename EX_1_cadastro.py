# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("|----------------------------------|")
print("|-------- CADASTRO ----------------|")
print("|----------------------------------|")
cadastros=[]
nome=input("DIGITE O NOME:")
idade=input("DIGITE A SUA IDADE:")
email=input("DIGITE O SEU EMAIL:")
senha=input("DIGITE A SUA SENHA:")
#DADOS CADASTRADOS
print("\n--- DADOS CADASTRADOS ---")
cadastros.append(nome)
cadastros.append(idade)
cadastros.append(email)
cadastros.append(senha)
for pessoa in cadastros:
    print(pessoa)