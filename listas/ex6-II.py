sh = float(input())
h = float(input())
sb = sh * h
inss = sb * (8 / 100)
sind = sb * (5 / 100)
sl = sb - (sb * 11 / 100) - inss - sind
print(f"Salário bruto: R$ {sb:.2f}")
print(f'INSS: R$ {inss:.2f}')
print(f'Sindicato: R$ {sind:.2f}')
print(f'Salário liquido: R$ {sl:.2f}')

