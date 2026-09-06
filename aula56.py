"""

split e join com list e str
split - divide uma string
join - une um string

"""

frase = "Olha só que coisa interessante"
lista_palavras = frase.split() #Dá para adicionar caracter que voce quer dividir dentro do split
print(lista_palavras)

for i, frase in enumerate(lista_palavras):
    print(lista_palavras[i].lstrip()) #Corta espaços, direito e esquerdo
    
    
# Listas de listas

salas = [
    ['Maria', 'Helena'],
    ['Elaine'],
    ['Tyla']
]
print(salas[2][0])

for sala in salas:
    for aluno in sala:
       print(aluno) 