"""

Introdução ao desacomplamento + tuplas

"""

nomes = ['Maria', 'Helena', 'Luiz']
nome1, nome2, nome3 = nomes # vai receber na ordem

nome1, *_ = ['Marcia', 'Marcio', 'Outros']

*_, nome2, _ = ['Manolos', 'Gabs', 'Selma', 'Jose']
print(nome2)