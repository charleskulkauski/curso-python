"""

Calculadora com while

"""
num1 = 0
num2 = 0

while True:
    primeiro_num = input('Digite o primeiro numero:')
    segundo_num = input('Digite o segundo numero: ')
    operador = input('Digite o operador (+ - / *): ')
    
    numeros_validos = None
    try:
        num1 = int(primeiro_num)
        num2 = int(segundo_num)
        numeros_validos = True
    except Exception as error:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Numeros digitados são inválidos')
        continue
    
    
    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Operador invpalido')
        continue
    
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '/':
        resultado = num1 / num2
    elif operador == '*':
        resultado = num1 * num2   
    else:
        print('Digite o operador corretamente!')
        continue 
    
    print(f'RESULTADO: {resultado}')
        
    sair = input("Quer sair? [s]im:").lower().startswith('s')
    if sair is True:
        break

    