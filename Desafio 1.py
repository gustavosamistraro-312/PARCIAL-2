# Programa que soma dois números

# Função que recebe dois números e retorna a soma deles
def somar(a, b):
    return a + b  # retorna a soma de a e b

# Entrada do primeiro número digitado pelo usuário
numero1 = float(input("Digite o primeiro número: "))

# Entrada do segundo número digitado pelo usuário
numero2 = float(input("Digite o segundo número: "))

# Chama a função somar e guarda o resultado
resultado = somar(numero1, numero2)

# Mostra o resultado da soma
print(f"A soma de {numero1} e {numero2} é {resultado}.")
