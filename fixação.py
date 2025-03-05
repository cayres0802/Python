#nm = [2, 4, 6, 8]
#for a in nm:
#    c = a * a
#    print(c)

# nm = int(input("Digite um número: "))

# while nm != -1:
#     print(nm)
#     nm -= 1
    
try:
    num = int(input("Digite um numero: "))
    x = 100 / num
    print(x)
except ZeroDivisionError:
    print("Erro! Não é possivel dividir por zero")