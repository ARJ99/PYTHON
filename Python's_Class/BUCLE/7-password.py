"""Ejercicío: Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta."""


Keyword="Alejo99"
password = input("Type the password : ")

while password != Keyword:
    if password != Keyword:
        print("Access Denied, Try again.")
        password=input("Type the password: ")
else:
    print("Access Granted")    

    
    

