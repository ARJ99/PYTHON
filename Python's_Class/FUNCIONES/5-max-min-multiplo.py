"""Ejercicio: Escribir una función que calcule el máximo común divisor de dos números y otra que calcule el mínimo común múltiplo.

Minimo común multiplo:
El mínimo común múltiplo {m.c.m} de dos números a y b es el multiplo más pequeño entre a y b.

Maximo común divisor:
El máximo común divisor, {m.c.d}. de dos o más números, es el mayor número que divide a todos de manera exacta. Es decir su resto es 0.



"""
def mcm(x,y):
    z = max(x,y) # Se usa el max por que es seguro que el num mayor tenga el mcm del numero menor.

    while True:
        if (z % x == 0) and (z % y == 0): # De está forma hallamos el mcm
            return z
        z +1

print(mcm(2,4))          

def mcd(n, m):

    rest = 0
    while(m > 0):
        rest = m
        m = n % m
        n = rest
    return n

print(mcd(4,8))    