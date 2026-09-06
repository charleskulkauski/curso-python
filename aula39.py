"""
Iterando strings com while

"""

nome = False

while nome == False:
    nome = input('Digite seu nome: ')
    if (len(nome) == 0):
        nome = False
        print('Voce nao digitou nada, tente novamente')   
        
tamanho_nome = len(nome)-1
novo_nome = ''
contador = 0

while contador <= tamanho_nome:
    novo_nome += '*'
    novo_nome += nome[contador]
    contador += 1
    
print(f'Novo nome = {novo_nome}')