"""

Calculo 2 digito CPF

"""

# Calculo 1 digito

# cpf = input('Digite seu cpf: ')
cpf = '982.215.318-04'

cpf = cpf.replace(".","")
cpf_antes_traco = cpf.split("-")[0]
lista_cpf_antes_traco = list(cpf_antes_traco)

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

# CALCULO 2 DIGITO

cpf = cpf.replace("-", "")
digitos_necessarios = cpf [:10]
resultado_multiplicacao = []
resultado_soma = 0
resto = 0

cont = 11
for i, numero in enumerate(digitos_necessarios):
    resultado_multiplicacao.append(int(numero) * cont)
    cont -=1
    
for i, numero in enumerate(resultado_multiplicacao):
    resultado_soma += numero
    
resultado_soma *= 10
resto = resultado_soma % 11

total = 0 if resto > 9 else resto

print(f"Primeiro digito: {resultado}\n Segundo digito: {total}")
    


