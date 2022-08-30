"""List Comprehension:

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

The Syntax
newlist = [expression for item in iterable if condition == True]

Puedes usar la Syntax sin condicíon.

"""
#----------------------------------------------------------------
#Ejercicío: crear una lista con los cuadrados de los números entre 1 y 5, podríamos hacerlo con el siguiente bucle for:

list = [1,2,3,4,5]
newlist = [ i **2 for i in list ]
print(newlist, end="\n\n")

#end ="\n" Sirve para crear una linea de espacion entre prints, se puede repetir \n el numero de veces deseas para el espacío.

#----------------------------------------------------------------

#Ejercicío: Crear list de numero del 1 al 10 y elevarlos al 3.

list3 = [ i **3 for i in range (1,11)]

print(list3)

#---------------------
