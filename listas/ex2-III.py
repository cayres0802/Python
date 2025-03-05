conta = int(input('Conta: '))
vp = int(input('Pagamento: '))
troco = vp - conta
notas = [50, 20, 10, 5, 2, 1]
for i in notas:
    while troco >= i:
        print(f'Uma nota de {i}')
        troco -= i