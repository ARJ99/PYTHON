"""Ejercicio: Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función."""
from math import pi
import math

def circle_area(radius):
    return  math.pi*pow(radius,2)
    

def cilinder(radius,high):
    #return  2 * math.pi * radius *(radius + high)
    outcome = circle_area(radius) * high
    return round(outcome,3)


print(cilinder(4,4))    

""" La funcion cilinder y circle_area comparte el mismo argumento por lo cual, al llamar al final la funcion cilinder con 2 argumentos la consola acepta tambien a la primera funcion circle_area."""