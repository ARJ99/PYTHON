# Ejercicio: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

# key = "alejo1499"

# password = input(" Insert password :")

# password= password.casefold()

# print("Access granted") if password == key else print("Access denied")

#------------------------------------------------------------------------
#Mismo ejercicio pero con 2 posibles contraseñas.

key1 = "alejo1499"
key2 = "byron1012"

password = input("Insert password :")

password = password.casefold()

print("Access granted") if password == key1 else print("Access granted") if password == key2 else print("Access denied")
#-------------------------------------------------------------------------
#Mismo ejercicio pero usando OR
# key1 = "alejo1499"
# key2 = "byron1012"

# password = input("Insert password :")

# password = password.casefold()

# if password == key1 or password == key2:
#     print("Access granted")
# else:
#     print("Access denied")