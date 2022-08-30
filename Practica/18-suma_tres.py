# Ejercicio 18: Calcular la suma de tres números, é incluír una condición de igualdad.

def sumar_num(a, b, c):
    suma= a + b + c
    """ Calcula la suma de 3 números"""

    if a == b and a == c:   
        # Ley de transitividad. SI a = b y a = c, entonces b = c.
        suma *= 3

    return suma    

print(sumar_num(2, 2 , 7))
print(sumar_num(2, 2 , 2))