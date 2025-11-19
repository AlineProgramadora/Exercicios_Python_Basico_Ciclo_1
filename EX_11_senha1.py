# Escreva um programa que pede que o usuário informe uma senha.
# O código deve comparar a senha informada pelo usuário com uma senha pré-definida no código armazenada em uma variável 
# Depois o código deve informar se a senha é correta ou incorreta.

# OUTPUT ESPERADO
# Exemplo 1:

# Digite a senha: 123123
# Senha incorreta

# Exemplo 2:

# Digite a senha: AC12
# Senha correta

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
# Sistema de verificação da  senha 🔑
senha_correta = "AC12"  # Senha pré-definida no código
senha_informada = input("Digite a senha: ")
# Verificando se a senha está correta ou incorreta aqui
senha_valida = senha_informada == senha_correta
# Exibindo o resultado 🔐
if senha_valida:
    print("Senha correta ✅")
else:
    print("Senha incorreta ❌")
