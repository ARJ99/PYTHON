"""Ejercicio: Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Despúes debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>."""

nombre = input('¿Cómo te llamas? ')
edad = input('¿Cuántos años tienes? ')
direccion = input('¿Cuál es tu dirección? ')
telefono = input('¿Cuál es tu número de teléfono? ')

datos ={
"nombre":nombre,
"edad":edad,
"direccion":direccion,
"telefono":telefono    
}

print(datos['nombre']," tiene ",datos['edad']," años y vive en",datos['direccion'],", además, su telefono es: ",datos['telefono'])