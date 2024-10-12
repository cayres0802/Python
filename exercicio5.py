# Exercicio 1

# n = float(input("Digite um número inteiro: "))

# if n % 1 != 0: 
#     print(f"{n} não é um número inteiro")
# elif n % 2 == 0:
#     print("par")
# else:
#     print("impar")

# Resolução 1
# n = input('Digite um número: ')

# if n.isdigit():
#     n_int = int(n)
#     par = n_int % 2 ==0
#     par_texto ='impar'
    
#     if par:
#         par_texto = 'par'
        
#     print(f'O número {n_int} é {par_texto}')
# else:
#     print('Você não digitou uma número inteiro')

# Exercicio 2
# hora = int(input("Que horas são?"))

# if 0 <= hora <= 11:
#     print("Bom dia!")
# elif 12 <= hora <= 17:
#     print("Boa tarde!")
# else:
#     print("Boa noite!")

# Resolução 2
# n = input("DIgite a hora: ")

# try:
#     hora = int(n)
    
#     if hora >= 0 and hora <= 11:
#         print('Bom dia')
#     elif hora >= 12 and hora <= 17:
#         print('Boa tarde')
#     elif hora >= 18 and hora <= 23:
#         print('Boa noite')
#     else:
#         print('Não conheço essa hora')
# except:
#     print('Por favor, digite apenas numeros inteiros')
    
# Exercicio 3
# nome = input("Qual o seu primeiro nome? ")

# if len(nome) <= 4:
#     print("Seu nome é curto.")
# elif len(nome) == 5 or len(nome) == 6:
#     print("Seu nome é normal.")
# else:
#     print("Seu nome é muito grande.")

# Resolução 3

# nome = input('Digite seu nome: ')
# tamanho = len(nome)

# if tamanho > 1:
#     if tamanho <= 4:
#         print('seu nome é curto')
#     elif tamanho >= 5 and tamanho <= 6:
#         print('seu nome é normal')
#     else:
#         print('Seu nome é grandeg')
    
# else:
#     print('Por favor, digite mais de uma letra')