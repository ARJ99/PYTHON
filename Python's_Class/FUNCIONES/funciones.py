
# Funcionamiento de una funcion
""" 
Creas una funcion con la keyword (def) y dentro del parenthesis puedes poder todos los parametros que deseas, separados por una coma. Debes mandar a llamar la funcion y poner una valor al argumento para ejercutar la funcion.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.



"""



#Funcion con 1 Argumento

# def my_function(fname):
#   print(fname ," Rios",sep='-->')

# my_function("Emilio")
# my_function("Tobias")
# my_function("Luis")

#-----------------------------------

#Funcion con 2 argumentos

# def my_function(fname, lname):
#   print(fname + " " + lname)

# my_function("Alejandro", "Rios")

#------------------------------------------------------------
""" Funcion N cantidad de Argumentos.
Si no sabes cuantos argumentos vas a necesitar, puedes poner un * delante del nombre del main argument y pero debes especificar luego la posicion del argumento que quieres mandar a llamar."""
#Ejemplo:

# def my_function(*kids):
#   print("The youngest child is " + kids[1])

# my_function("Emilio", "Tobias", "Linus")

#------------------------------------------------------------
"""Tú puedes usar tambien la sintaxis keys= values
 Ejemplo:"""

# def my_function(child1, child2, child3):
#     print("The youngest child is :" +child2)

# my_function(child1 = "Camilo", child2= "Alejandro", child3="Diego")    

#------------------------------------------------------
#Ejemplo: Funcion sin argumentos.
# def imprimir_mens():
#     print("Mensaje especial")
#     print("Estoy aprendiendo a usar Funciones!")

# imprimir_mens()

#---------------------------------------------------------------------
#Ejemplo: Función con 1 Argumento.

# def conversacion(mensaje):
#     print("Hola")
#     print("Cómo estás?")
#     print(mensaje)
#     print("Adiós")


# opcion =int(input("Elige una opcion(1,2,3):"))
# if opcion == 1:
#     conversacion("Elegiste la opcion 1")
# elif opcion ==2:
#     conversacion("Elegiste la opcion 2")
# elif opcion ==3:
#     conversacion("Elegiste la opcion 3")
# else:
#     print("Escribe la opcion correcta")     
# 
# -----------------------------------------------------------------
#Ejercicio:  Funcion con 1 Argumento.

def greetings(tipodesaludos):
    print("You will watch a greeting")
    print(tipodesaludos)  


opcion =int(input("Choose a number for a greeting(1,2,3):")) 
if opcion == 1:
    greetings("Howdy!")
elif opcion ==2:
    greetings("What's up!")
elif opcion ==3:
    greetings("How have you been?")    
else:
    print("Type other choice")        