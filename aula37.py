"""
Repetições
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira

"""

i = 0

while i < 10:
    i += 1
    
    if i == 6:
        print('Não vou mostrar o 6')
        continue
    
    print(i)