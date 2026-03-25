# Programa que soma dois números

# Função para somar dois números
def somar(a, b):
    return a + b  # retorna a soma dos dois números

# Entrada dos números
numero1 = float(input("Digite o primeiro número: "))  # recebe o primeiro número
numero2 = float(input("Digite o segundo número: "))  # recebe o segundo número

# Chama a função de soma e exibe o resultado
resultado = somar(numero1, numero2)  # calcula a soma
print(f"A soma de {numero1} e {numero2} é {resultado}.")  # mostra o resultado
