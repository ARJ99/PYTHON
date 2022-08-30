""" Ejercicio:  Ejercicio
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados."""

import math

def square(instance):

    list = []
    for i in (instance):
        list.append(pow(i,2))  #El built-in method pow(numero,potencia) Sirve para sacar el cuadrado.

    return list    


print(square([2,4,6,8])) 

