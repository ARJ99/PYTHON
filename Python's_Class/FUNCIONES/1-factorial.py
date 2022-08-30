""" Ejercicio:
Escribir una función que reciba un número entero positivo y devuelva su factorial."""


# def factorial(num):
#     a = 1
#     for i in range(1,num):
#         a *= i+1
        
#     return a    
    
# print(factorial(4)) 
#----------------------------------------------------------
#Ejercicio con diferente solución.
def fact(num):

    for i in range(1,num):
        num= num*i
 
    return num

print(fact(4)) 