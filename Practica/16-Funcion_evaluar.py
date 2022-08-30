#Ejercicio 16 : Crear una funcion para evaluar un número y realizar  una operación

# def difference(n):
    
#     if n <=15:
#         return 15- n
#     else:
#         return (15 - n)*2    

# print(difference(17))        
# print(difference(3))        

#-------------------------------------------------------------
# Ejemplo: Calcule la el promedio de notas parar varios estudiantes.

def puntuacion(clase):
    return sum(clase)/ len(clase)

#Primera forma de resolverlo
clase = [7, 8, 9]
media = puntuacion(clase)
print("El promedio de la materia es  : {}".format(media))    

#Segunda forma de resolverlo 
print("El promedio de notas es :",end="")
print(puntuacion(clase = [7, 8, 9]))

#Tercera forma de resolverlo
print("El promedio es: ",puntuacion(clase = [7, 8, 9]))