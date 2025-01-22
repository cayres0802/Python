p = float(input("Peso em kg:"))
multa = (p - 50) * 4
if p > 50:
    print('Excesso')
    print(f'Multa: R$ {multa:.2f}')
else:
    print('Zero')