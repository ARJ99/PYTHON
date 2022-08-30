## Ejercicio Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. 

factura = {} # Esto es un diccionario. Por dentro guarda key=value 
Options=""


while Options !="T":
    Options = input("Que funciones deseas realizar: Añadir factura (A) Pagar Factura (P) ó Terminar proceso (T): ")

    if Options == "A": #Añadir factura al diccionario
        clave = input("Digite el número de la factura: ")
        coste = int(input("Digite el valor de la factura: "))
        factura[clave] = coste # Aqui agrego por 1 vez el key(clave) y el value(coste) al diccionario.
        print("La factura fue agregada con exito.")
        
    elif Options == "P" : #Pagar factura almacenada en el diccionario.
        clave2 = input("Digite el número de la factura: ")
        otra_factura =input("Deseas agregar otra factura para el pago? (Si/No) ")
        if otra_factura =="Si":
            clave3 = input("Digite el número de la factura: ")
            print("El valor de la factura ",factura.keys(), "es: ",factura.get(clave3)+factura.get(clave2))
        else:
            #El built-in metodo name_diccionario.get("key") Sirve para mandar a llamar mediante el Key su respectivo value dentro del diccionario.
            print("El valor de la factura ",clave2, "es: ",factura.get(clave2))
            
else: # Terminacion del proceso.
    print("Gracias por su tiempo. ")
           

    


           
    

    
    



