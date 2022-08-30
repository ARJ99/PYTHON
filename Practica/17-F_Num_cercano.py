# Ejercicio 17: Crear una función para determinar si un número es cercano a 1000 ó a 2000. Que no se separe 100 unidades.

def nearby(n):
    """ Comprueba si una número es cercano a 1 mil ó 2 mil."""
    return (abs(1000-n)< 100) or (abs(2000-n)<100)

print(" This is a trial or a Demo for 1000")

print(nearby(1000))
print(nearby(950))
print(nearby(200))

print(" This is a trial or a Demo for 2000")

print(nearby(2000))
print(nearby(1950))
print(nearby(3000))