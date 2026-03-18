capital = float(input("Digite o capital (C): "))
taxa = float(input("Digite a taxa de juros (I): "))
tempo = float(input("Digite o tempo (T): "))

juros = (capital * taxa * tempo) / 100

print("O valor dos juros é:", juros)
