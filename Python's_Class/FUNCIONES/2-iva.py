"""Ejercicio: Ejercicio
Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
"""

def iva(amount, percent =21):
    return amount * percent/100

print(iva(500000))
print(iva(10000,10))    