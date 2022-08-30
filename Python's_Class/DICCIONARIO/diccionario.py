
#..EJEMPLO IMPRIMIENDO EL CONTENIDO DE LAS LLAVES. 
# mi_diccionario = {
#         'llave1' :1,
#         'llave2' :2,
#         'llave3' :3,
#     }

# print(mi_diccionario['llave1'])   
  

#-----------------------------------------------------------
#..Ejercicio par obtener Values From Diccionaries
#Syntax
#x = name_dict.values()
#Esta sytax te mostrará todos los valores del diccionario.

#-----------------------------------------------------------
#..Ejercicio para obtener Keys from Diccionaries
#Syntax
#x = name_dict.keys()

#Esta Syntax te mostrará todos las Keys del diccionario.



#-----------------------------------------------------------
#..Ejercicio para crear un loop(FOR) con los keys=values del diccionario.
# numeros_favoritos = {
#         'Alejo': 14,
#         'Diego': 27,
#         'Mamá': 25,
# }
#*El uso de las iteraciones con nombre(persona y valores) se usan para referirse a Key y Values. Para que funcione de está manera, En el for.. in.. debes llamar al nombre_diccionario.items()

# for persona,valores in numeros_favoritos.items():
#     print(persona + ' tiene este número : ' + str(valores))

#--------------------------------------------------
#..Ejemplo: 
# poblacion_pais={
#     'Argentina':4938712 ,
#     'Colombia': 210147125,
#     'Brasil': 50372424,
# }

# for pais,poblacion in  poblacion_pais.items():
#     print(pais + "tiene" + str(poblacion) + "habitantes.")

#-----------------------------------------------------------
#..Ejemplo: Haciendo operaciones entre values del dicc.
numbers={"item1":2,"item2":3}

print(numbers["item1"]*numbers["item2"])




