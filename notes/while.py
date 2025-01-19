#usado quando vc quer repetir algo até que uma condição seja falsa
#cuidado para não criar um loop infinito
#verifica uma condição antes de cada iteração
#pode usar break para interromper o loop mesmo que a condição ainda seja verdadeira

i = 1
while i <= 5:
    print(i)
    i += 1
    
senha = ""
while senha != "python123":
    senha = input("Digite a senha: ")
print("Senha correta, bem-vindo!")

while True:
    nome = input("Digite seu nome (ou 'sair' para parar): ")
    if nome.lower() == "sair":  # Verifica se o usuário digitou "sair"
        break
    print(f"Olá, {nome}!")