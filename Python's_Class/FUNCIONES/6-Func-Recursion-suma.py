#Ejercicio: Sumatoria recursiva. Es como un ciclo while pero sin ciclos.


def sumatoria(num):
    if num == 1:
        return 1

    else:
        return num + sumatoria(num-1)

""" Podemos hacer un input para una funcion de la siguiente manera:"""        

num = int(input("Digite un número para la sumatoria recursiva: "))
print(sumatoria(num))            

#Ejercicio: Factorial recursivo.

def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero-1)    

numero = int(input("Digite un número para el factorial recursivo: "))
print(factorial(numero)) 


