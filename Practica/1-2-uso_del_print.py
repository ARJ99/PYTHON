# Ejercicio 1: Mostrar en pantalla el uso de la funcion print

#El argumento 'end' en la funcion print, nos permite cambiar el final del print
#Para este caso, en lugar del salto de pagina comun, remplazaremos ese salto por 
#un espacio y así se ejecutara los dos prints en la mísma linea.

print('Lets get together ', end='  ')
print('Lets get together ')

#--------------------------------------------------------

#El argumento sep, nos permite separar valores dentro del print con lo que deseemos.
print('Python','es', 'lo mejor',sep='--')

#--------------------------------------------------------
#El Argumento format nos permite llenar valor luego (place holders).

print('{} es {}'.format('Python','Tremendo'))

#---------------------------------------------------------
# Ejercicio 2: Crear un diccionario y mostras sus keys, values or both.
diccionario= {
   "Luis" : "Rios",
   "Diego" : "Rios"
}
#x= diccionario.get("Luis")
#x= diccionario.keys()
#x= diccionario.values()
x= diccionario.items()
print(x)
