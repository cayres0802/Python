n1 = float(input())
n2 = float(input())
n3 = float(input())

if n1 > n2 and n1 > n3:
    print(f'Maior {n1}')
elif n2 >= n3:
    print(f'Maior {n2}')
else:
    print(f'Maior {n3}')
    
if n1 < n2 and n1 < n3:
    print(f'Menor {n1}')
elif n2 <= n3:
    print(f'Menor {n2}')
else:
    print(f'Menor {n3}')