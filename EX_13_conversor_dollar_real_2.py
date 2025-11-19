# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("Escolha uma opção: ")
print("1 - Dollar para Real") # Dica: Se escolher 1, vai converter dólar para real
print("2 - Real para Dollar") # Dica: Se escolher 2, vai converter real para dólar
opcao = int(input("Digite a opção: "))
# Lembrete para mim: Se o usuário escolheu a opção 1 (Dólar para Real)
if opcao == 1:
    cotacao_dolar = float(input("Informe a cotação atual do Dollar: ")) 
    quantidade_dolar = float(input("Informe a quantidade de dólares: "))  
    valor_real = cotacao_dolar * quantidade_dolar 
    print(f"O valor em reais é R${valor_real:.2f}")
# Lembrete para mim : Se o usuário escolheu a opção 2 (Real para Dólar)
elif opcao == 2:
    cotacao_dolar = float(input("Informe a cotação atual do Dollar: ")) 
    quantidade_real = float(input("Informe a quantidade de reais: "))  
    valor_dolar = quantidade_real / cotacao_dolar 
    print(f"O valor em dólares é ${valor_dolar:.2f}")
# Lembrete para mim: Caso o usuário escolha uma opção inválida kkk
else:
    print("Opção inválida! ❌") 
