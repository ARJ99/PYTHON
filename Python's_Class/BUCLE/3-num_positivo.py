"""Ejercicío:
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares 
desde 1 hasta ese número separados por comas."""

# num = int(input("Ingrese un número:"))
# if num > 0:
#     for i in range(1,num+1,2):
#         print("El número {} es impar".format(i))


#-------------------------------------------------------------
#Mismo ejercio pero hecho de manera más precisa.
num = int(input("Ingrese un número:"))
if num > 0:
    for i in range(1,num+1):
        if i % 2 != 0:
            print("El número "+ str(i) + " es impar.")
else:
    print("Eliga un número positivo.")