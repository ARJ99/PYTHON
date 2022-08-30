"""Ejercicio: ## Ejercicio

Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
"""

# word = input("Digite una palabra: ")
# x = word.casefold()

# backward_word = x[::-1]
# print(backward_word)

# print("Es un palindromo: ",backward_word) if backward_word == word else print("No es un palindromo: ",word)

#--------------------------------------------------------------
"""Mismo ejercicíon diferente solución:"""
palabra = list(input("Digite una palabra: "))
word= palabra
word.reverse()
if word == palabra:
    print("Es un palindromo.")
else:
    print("No es palindromo.")    
