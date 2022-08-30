"""Ejercicío: Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario."""

Currency = {
"Euro":"€",
"Dollar":"$",
"Yen":"¥"
}

Inquiry = input("Digite una moneda: ")
print(Currency.get(Inquiry.capitalize(),"La divisa no está."))
#El metodo get en diccionarios, nos sirve para obtener usando una key su respectivo value.
#Si en el diccionario la key no está, por medio de la coma se imprimira una mensaje en caso de no haber ninguna key que coincida. Es similar al proceso del "else".