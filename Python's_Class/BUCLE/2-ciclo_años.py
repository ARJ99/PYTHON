"""Ejercicio: Escribir un programa que pregunte al usuario su edad y muestre por pantalla " ha cumplido 1,2 años",etc (desde 1 hasta su edad)."""

Age=int(input("How old are you? "))

for i in range(Age):
    print("Has cumplido :"+str(i+1) + " años")
