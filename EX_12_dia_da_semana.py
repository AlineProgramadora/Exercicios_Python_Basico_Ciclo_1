# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
# Programa para identificar o dia da semana 📅
# ai eu vou pedir o número correspondente ao dia da semana
numero = int(input("Digite um número (1 a 7): "))
dias_da_semana = {
    1: "Domingo",
    2: "Segunda",
    3: "Terça",
    4: "Quarta",
    5: "Quinta",
    6: "Sexta",
    7: "Sábado"
}

# Verificando e exibindo o resultado 📍
if numero in dias_da_semana:
    print(dias_da_semana[numero])  # Mostra o dia correspondente
else:
    print("Número errado ❌")  # Caso o número não esteja no intervalo de 1 a 7
