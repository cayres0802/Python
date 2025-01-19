L = [1, 7, 4, 12, -2]
x = L[0]  # Inicializa x com o primeiro elemento da lista (1)
while True:
    L = L[1:]  # Remove o primeiro elemento da lista
    if not L:  # Verifica se a lista está vazia
        break  # Sai do loop infinito quando a lista estiver vazia
    if L[0] > x:  # Compara o primeiro elemento restante com x
        x = L[0]  # Atualiza x com o maior valor encontrado
print(x)
