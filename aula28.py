nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")


if (nome and idade):
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    
    if (nome.find(' ') == True):
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f"a primeira letra do seu nome é {nome[0]}")
    print(f"a ultima letra do seu nome é {nome[-1]}")
    
else:
    print("Desculpe, voce deixou campos vazios")