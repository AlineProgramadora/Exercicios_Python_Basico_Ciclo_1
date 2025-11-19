# Faça uma atualização no código do exercício anterior, agora o programa deve exibir o nome do produto, o valor do desconto e o valor final do produto.

# OUTPUT ESPERADO:

# Produto: FIAT TORO
# Preço: 200000
# Porcentagem de desconto: 15
# O FIAT TORO com 15.0% de desconto custará R$ 170000.0

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

# Programa que calcula o valor do desconto e o preço final

produto = input("Produto: ")
preco = float(input("Preço: "))
desconto_percentual = float(input("Porcentagem de desconto: "))

# Calculando o desconto
desconto = preco * (desconto_percentual / 100)

# Preço final após o desconto
preco_final = preco - desconto

# Mostrando o resultado
print(f"O {produto} com {desconto_percentual}% de desconto custará R$ {preco_final}.")

#Produto: FIAT TORO
#Preço: 200000
#Porcentagem de desconto: 15
#O FIAT TORO com 15.0% de desconto custará R$ 170000.0 na calculadora 
