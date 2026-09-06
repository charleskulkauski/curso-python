# Listas em python
# Dado mutável
# Suporta vários valores de qualquer tipo
# Conhecimento reutilizaveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, create, read, update, delete


lista = [10,20,30]
lista[2] = 300
del lista[2]
print(lista)

lista.append(50)
print(lista)

lista.pop()
print(lista)

lista.inset(0, 5) # Adiciona um valor num indice especifico (indice,valor)
print(lista)


lista_a = [0,1]
lista_b = [2,3]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b) # Mexe diretamente na lista A e insere nela

lista_e = ['e', 'f']
lista_f = lista_e
print(lista_f)

lista_e[0] = 'Outra coisa'
print(lista_f)

lista_g = lista_e.copy()
lista_e[1] = 'Alterado dnv'
print(lista_g)