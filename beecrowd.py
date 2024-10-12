# Lê o valor monetário com duas casas decimais

N = float(input())
=======
N = float(input("Digite o valor: "))
>>>>>>> d2230174c4ef1f495cf3faea8bccec9564d7247a

# Multiplica o valor por 100 para evitar problemas com precisão de ponto flutuante
valor = int(N * 100)

# Lista das notas e moedas em centavos
notas = [10000, 5000, 2000, 1000, 500, 200]
moedas = [100, 50, 25, 10, 5, 1]

# Calcula a quantidade de cada nota
quantidade_notas = []
for nota in notas:
    quantidade_notas.append(valor // nota)
    valor %= nota

# Calcula a quantidade de cada moeda
quantidade_moedas = []
for moeda in moedas:
    quantidade_moedas.append(valor // moeda)
    valor %= moeda

# Imprime a quantidade de cada nota
print("NOTAS:")
print(f"{quantidade_notas[0]} nota(s) de R$ 100.00")
print(f"{quantidade_notas[1]} nota(s) de R$ 50.00")
print(f"{quantidade_notas[2]} nota(s) de R$ 20.00")
print(f"{quantidade_notas[3]} nota(s) de R$ 10.00")
print(f"{quantidade_notas[4]} nota(s) de R$ 5.00")
print(f"{quantidade_notas[5]} nota(s) de R$ 2.00")

# Imprime a quantidade de cada moeda
print("MOEDAS:")
print(f"{quantidade_moedas[0]} moeda(s) de R$ 1.00")
print(f"{quantidade_moedas[1]} moeda(s) de R$ 0.50")
print(f"{quantidade_moedas[2]} moeda(s) de R$ 0.25")
print(f"{quantidade_moedas[3]} moeda(s) de R$ 0.10")
print(f"{quantidade_moedas[4]} moeda(s) de R$ 0.05")
print(f"{quantidade_moedas[5]} moeda(s) de R$ 0.01")
