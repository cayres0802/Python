n = int(input())
i = 1
while i * (i + 1) * (i + 2) < n:
    i = i + 1
print(i*(i + 1) * (i + 2) == n)
    