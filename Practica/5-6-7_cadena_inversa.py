# Ejercicio 5: Obtener la representacion inversa de una cadena

# cadena="python"

#for i in range(len(cadena)-1,-1,-1):
   # print(cadena[i],end=' ')

#----------------------------------------------
#print()
# print(cadena[::-1])

#-----------------------------------------------
#Ejercicio 6: Obtener un conjunto de números separados por coma y crear lista
#Metodo split para separar strings 
# entrada= input('Escriba varios número separados por coma :')

# numeros= entrada.split(',')
# print(numeros)


#-------------------------------------------------
#Ejercicio 7:
# Obtener la extension de un archivo cualquiera que dijite el usuario.

string=input('Ingrese el nombre y extension de un archivo')

new_string=string.split('.')
print(new_string[-1])

#Las string son a data type list.
print(type(new_string))
