""" Ejercicio: Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará."""
word= input("Digite una palabra: ")
while word != "salir":
    if word == "salir":
        break
    else:
        print(word)
        word= input("Digite una palabra: ")
#---------------------------------------------------------------

while True:
    word= input("Digite una palabra: ")
    if word  == "salir":
        break
    else:
        print(word)