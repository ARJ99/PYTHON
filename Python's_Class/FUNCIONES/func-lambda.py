"""
..Definición de Lambda

En Python, una función Lambda se refiere a una pequeña función anónima. 
Las llamamos “funciones anónimas” porque técnicamente carecen de nombre.

Al contrario que una función normal, no la definimos con la palabra clave
estándar def que utilizamos en Python. En su lugar, las funciones Lambda
se definen como una línea que ejecuta una sola expresión. Este tipo de 
funciones pueden tomar cualquier número de argumentos, pero solo pueden 
tener una expresión.

..Syntax
lambda arguments : expression

#Como mejor te lo puedo explicar es enseñándote un ejemplo básico, vamos a ver una función normal y un ejemplo de Lambda:

-Aquí tenemos una función creada para sumar.
def suma(x,y):
    return(x + y)

-Aquí tenemos una función Lambda que también suma.
lambda x,y : x + y
#Para poder utilizarla necesitamos guardarla en una variable.
suma_dos = lambda x,y : x + y

//Ejercicio: Curdrado de un número:

cuadrados = lambda x : x **2
print(cuadrados(4))

"""
#---------------------------------------------------------------------
#.. USOS DE LA FUNCION LAMBDA:

""" #.. LAMBDA EN LISTAS CON EL METODO FILTER()
 La función filter() es capaz de devolver una nueva colección con los elementos filtrados que cumplan una condición.

..Syntax
filter(function, iterable)

 """

#Tengo una lista con muchos números
#comprobar = [38,24,99,42,2,3,11,23,53,21,3,53,77,12,34,92,122,1008,26]
#Creo una variable y le aplico filter() y la lambda
#valores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#pares = list(filter(lambda x : x % 2 == 0, valores))
#print(pares)

#------------------------------------------------------------------------
#.. USO DE LA FUNCION LAMBDA CON MAP()

""" #- map()
La función map() en Python aplica una función a cada uno de los elementos de una lista."""

#enteros = [1, 2, 4, 7]
# cuadrados = list(map(lambda x : x ** 2, enteros))
# print(cuadrados)
# [1, 4, 16, 49]

#------------------------------------------------------------------------
"""#..USO DE LA FUNCION LAMBDA CON REDUCE()
Esta función se utiliza principalmente para llevar a cabo un cálculo acumulativo sobre una lista de valores y devolver el resultado."""


#-la suma acumulativa de esta lista, la puedes calcular de la siguiente manera:

# valores = [2, 4, 6, 5, 4]
# suma = 0
# for i in valores:
#     suma = suma + i
# print(suma)

#Pero también puedes usar la funcion reduce()

#from functools import reduce

#valores = [2, 4, 6, 5, 4]
#suma = reduce(lambda x, y: x + y , valores)
#print(suma)

