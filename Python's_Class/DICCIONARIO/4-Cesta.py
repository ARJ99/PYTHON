"""Ejercicío: Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato."""

cesta = {} #Creamos un diccionario vacio.
continuar = True # Almost every variable is true, except if the variable is empty in that case the Boolean will be False.

while continuar: #Es lo mismo que decir--> while Continuar = True:
    item = input('Introduce un artículo: ')
    precio = float(input('Introduce el precio de ' + item + ': '))
    cesta[item]= precio # Se usa para agregar Key= Value al Diccin.
    continuar= input("Deseas continuar (Si/No)")=="Si" 
    #Si la respuesta es un(No), el input return False y valor de continuar ahora será False y no se ejecutara más el codigo.
costo= 0
print("Lista de compras: ")
for item, precio in cesta.items():
    
    print( item, "\t", precio) 
    costo += precio
print("Valor Total: ",costo)       
    
#-----------------------------------------------
