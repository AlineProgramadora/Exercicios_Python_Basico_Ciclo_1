# Escreva um programa que pede ao usuário o preço de um produto e o valor de desconto em % e depois informe qual será o valor do desconto.
# Dica: 
# use a fórmula 
# desconto = preco * (porcentagem / 100) 
# para calcular o valor do desconto 

# OUTPUT ESPERADO:

# Qual o preço do produto? 300
# Qual a porcentagem de desconto? 10
# O produto que custa R$300.0 terá R$30.0 de desconto.

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


preco_produto = float(input("Qual o preço do produto? "))
percentual_desconto = float(input("Qual a porcentagem de desconto? "))

# para que eu possa calcular
desconto_calculado = preco_produto * (percentual_desconto / 100)

# Exibindo o valor do desconto aqui
print("O produto que custa R$", preco_produto, "terá R$", desconto_calculado, "de desconto.")
#tenho que por:
#Qual o preço do produto? 300 .Qual a porcentagem de desconto? 10 .O produto que custa R$ 300.0 terá R$ 30.0 de desconto.
