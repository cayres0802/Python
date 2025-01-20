l1 = float(input())
l2 = float(input())
l3 = float(input())

if l1 > l2 + l3 or l2 > l3 + l1 or l3 > l1 + l2:
    print("Não é um triangulo, um dos lados é maior que a soma dos outros dois lados")
elif l1 == l2 == l3:
    print("Triangulo equilatero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("Triangulo isósceles")
else:
    print("Triângulo escaleno")