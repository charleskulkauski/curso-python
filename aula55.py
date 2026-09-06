"""
Para calcular a cotna exata de numeros float

"""

import decimal

numero1 = decimal.Decimal('0.1')
numero2 = decimal.Decimal('0.3')
resultado = numero1 + numero2

print(resultado)
print(f'{resultado:.2f}')
print(round(resultado,2))
