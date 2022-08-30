"""Ejercicio :Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar."""

# Entero = int(input("Digite un número entero :"))

# if Entero % 2 == 0:
#     print("El {} es un número par".format(Entero))
# else:
#     print("El {} es un número impar".format(Entero))    


#----------------------------------------------------------------------------------
"""Mismo ejercicio con un SHORT HAND IF...ELSE"""

Entero = int(input("Digite un número entero :"))

print("El número {} es par".format(Entero)) if Entero % 2 == 0 else print("El número {} es impar".format(Entero))