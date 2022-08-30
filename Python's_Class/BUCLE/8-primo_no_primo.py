"""Ejercicío: Escribir un programa que pida al usuario un número entero positivo mayor que 2 y muestre por pantalla si es un número primo o no."""

number= int(input("Digite un número mayor a 2: "))
i=2

#Un primo es divisible por el mismo y por 1.
#Debemos probrar que el numero no sea divisible por todos los numeros anteriores a el mismo, por lo cual hay que aumentar i +1.
#
while number % i != 0: # Mientras que su resto sea 1 no sera divisible y debemos aumentar i +1 para probar el siguiente número.  
    i = i+1
if i == number: # Una vez sean igual, su resto sera 0, por lo cual su resultado será divisible.
    print("Es primo.")
else:
    print("No es primo.")   


    
"""  
7/2  7%2=1( No es divisible, es decir su resultado es un decimal.)
1|3,
--------
7/3  7%3=1 (No es divisible)
1|2,

--------
7/7  7%7 =0 (Es divisible)
0|1
"""
     


#--------------------------------------------------------------------
