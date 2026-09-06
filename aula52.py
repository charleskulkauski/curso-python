"""

Enumerate - enumera iteráveis (índices)

"""

lista = ['João', 'Pedro']
lista.append('Marcos')
lista_enumerada = enumerate(lista)

for item in lista_enumerada:
    print(item)
    
for indice, item in enumerate(lista):
    print(indice, item)
    
# Enumerate consome lista, ou seja após o for os valores dentro da lista 'esgotam'. quando atribuido a uma váriavel (exemplo linha 9)