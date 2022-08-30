""" Escribir un programa que pida al usuario dos números y devuelva su división. Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también."""

# dividendo= int(input("Digite el dividendo de la división :"))
# divisor= int(input("Digite el divisor de la división :"))


# print("No es divisible por 0") if divisor == 0 else print("Digite un número diferente") if divisor < 0 or dividendo < 0 else print("El resultado es :", dividendo/divisor)


#----------------------------------------------------------------------------------
"""Mismo ejercicio pero con condicionales clasicos"""


dividendo= int(input("Digite el dividendo de la división :"))
divisor= int(input("Digite el divisor de la división :"))

if divisor == 0:
    print("Error!")
else: 
    print("El resultado es :",dividendo/divisor)    