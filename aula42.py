frase = 'O python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Pyhton foi criada por Guido van Rossum. '
    
    
i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
        qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
        letra_apareceu_mais_vezes = letra_atual
    
    i+=1
    
print(f'A letra que apareceu mais vezes: {letra_apareceu_mais_vezes}')
print(f'Quantidade de vezes que apareceu: {qtd_apareceu_mais_vezes}')