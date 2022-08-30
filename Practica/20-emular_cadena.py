# Ejercicio 20 : Emular el funcionamiento de producto de cadena.
#Multiplicar la palabra deseada un número de veces indeterminadas.
def producto_cadena(cadena, repeticion):
    resultado = ""

    for i in range(repeticion):
        resultado += cadena
    return resultado    

print(producto_cadena("Python",3))
    
#--------------------------------------------------------

