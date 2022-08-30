"""Ejercicío:
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70

"""

Fruits = {
    'Platano':1.35, 'Manzana':0.8, 'Pera':0.85, 'Naranja':0.7
}

item = input("What fruits do you wish? ")
item=item.title()

if item in Fruits:
    print("La fruta ",item,"tiene un valor x kg:",Fruits.get(item))
    quantity = float(input("How much do you wish? "))

    print(quantity, "kg de ",item," tiene un valor total de: ",quantity*Fruits.get(item))

else:
    print("Lo siento, la fruta ",item," no está disponible.")    


