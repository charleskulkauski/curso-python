"""

Calculo primeiro digito CPF

"""

# cpf = input('Digite seu cpf: ')
cpf = '378.430.658-65'

cpf = cpf.replace(".","")
cpf_antes_traco = cpf.split("-")[0]
lista_cpf_antes_traco = list(cpf_antes_traco)
"""
outra forma:
nove_digitos = cpf[:9]

"""

resultado_multiplicacao = []

cont = 10
for i, numero in enumerate(lista_cpf_antes_traco):
    resultado_multiplicacao.append(int(numero)*cont)
    cont -= 1

resultado_soma = 0
for i, resultado in enumerate(resultado_multiplicacao):
    resultado_soma += resultado_multiplicacao[i]
    
resto = (resultado_soma*10) % 11
resultado = 0

if resto > 9:
    pass
else:
    resultado = resto
    
"""
outra forma:

resultado = resultado if resto <= 9 else 0

"""

    
print(f'Resultado final: {resultado}')

