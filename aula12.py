# Exercicio imc

nome = str(input("Digite seu nome: "))
altura=float(input("Digite sua altura: "))
peso = float(input("Digite seu peso:"))

def calculoimc(altura, peso):
    imc = peso/ (altura*altura) #ou -> altura**2
    
    return imc

print(f"Olá {nome}! Seu imc é: [{calculoimc(altura, peso):.2f}]")
