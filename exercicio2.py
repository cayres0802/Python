nome = "Maria"
altura = 1.59
peso = 44
imc = peso / (altura ** 2)

print(f"{nome} tem {altura} de altura, \npesa {peso}kg \ne seu IMC é {imc:.2f}")
print("{} tem {} de altura, pesa {}kg e seu IMC é {:.2f}".format(nome, altura, peso, imc))