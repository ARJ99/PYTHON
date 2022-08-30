""" Ejercicio: Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase."""

sentence = input("Type a phrase: ")
# word = input("type a letter: ")

contador = 0
# for i in sentence:
#     if i == word:
#         contador+=1
# print("La letra ", word, " se repite {}".format(contador))        
#----------------------------------------------------------------
# Metodo count() Sirve para contar el numero de veces que se repite un string.
x=sentence.count("a") 
print(x)



#----------------------------------------------------------------


# if "a" in sentence:
#     print("La letra \"a \" si esta en la oración.")
# else:
#     print("La letra \"a\" no esta en la oración.")