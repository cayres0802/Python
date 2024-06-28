#Fiz certinhoooo 
nome = input("Digite seu nome: ")
idade = input("DIgite a sua idade: ")

if nome and idade: 
    print(f"Seu nome é {nome} ")
    print(f"Seu nome invertido é {nome[::-1]}")
    print(f"Seu nome tem {len(nome)} letras.")
    print(f"A primeira letra do seu nome é {nome[:1]}")
    print(f"A última letra do seu nome é {nome[-1]}")

    if " " in nome:
        print(f"Seu nome contém espaços.")
    
    else:
        print("Seu nome não contém espaços.")

else:
    print("Desculpe, você deixou campos vazios.")




