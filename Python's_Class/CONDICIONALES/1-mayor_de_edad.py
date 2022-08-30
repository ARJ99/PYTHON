# Ejercicio: Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.

# CONDICIONALES TRADICIONALES

# Edad = int(input("Cuál es tú edad? "))

# if Edad >= 18:
#     print(" Access granted, Welcome buddy!")
# else:
#     print("Access denied, Sorry buddy. You're not old enough.")    

#----------------------------------------------------------
#SHORT HAND IF... ELSE
# Age = int(input("How old are you? "))

# print("Access granted, Welcome buddy!") if Age >= 18 else print("Access denied, Sorry buddy. You're not old enough")

#----------------------------------------------------------

Age = int(input("How old are you? "))

print("Access denied!") if Age < 18 else print("You're too old man, sorry" if Age >=50 else print("Access granted."))


