# Programa que verifica se um número é par ou ímpar

# Entrada do número
numero = int(input("Digite um número: "))  # recebe um número inteiro

# Verifica se é par
if numero % 2 == 0:  # se o resto da divisão por 2 for 0
    print("O número é par")  # mostra que é par
else:
    print("O número é ímpar")  # mostra que é ímpar
