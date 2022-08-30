""" Ejercicio:
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

num = int(input("Escriba un númeo para el conteo : "))

if num > 0:
    for i in range(num,-1,-1):  #Conteo regresivo en un FOR.
        print("Conteo regresivo: "+str(i))
       
else:
    print("Eliga un número entero.")