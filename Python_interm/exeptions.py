"""
.. EXEPCIONES:
-Se ejecuta en caso de errores.
..Try:  run this code in case of error
..Except: execute this code when there is an exception.
.. Else: No exception? Run this code.
.. Finally: Always run this code.

#--------------------------------------------
..Ejercicio Raise
-Sirve para mostrar un error al usuario en caso que no cumpla las condiciones establecidas para ejecutar el codigo.
"""
# x = -1
# if x < 0:
#     raise Exception("Solamente se puede un num positivo.")

#--------------------------------------------
"""
..Ejercicio TypeError:
-Se genera cuando se hace una operacion con un tipo de objeto incorrecto.

"""
# x = 4.2
# if not type(x) is int:
#     raise TypeError("Solamente se permite un num entero.")

#--------------------------------------------------------
"""
.. Ejericicio Assert:
-Se genera un Error si la expresion es evaluada como false.
-Syntax:  assert Condition, Mensaje en caso de Error.

Los Kelvin no pueden ser negativos, comienzan desde 0 grados.
Los Celcius empiezan desde -273°.
Para convertir Kelvin a Celcius,solo se resta 273.
"""
# def Celcius(Kelvin):
#     assert(Kelvin >=0),"Los grados Kelvin no son negativos."
#     return (Kelvin - 273)

# a = int(input("Digite un medida en Kelvin: "))
# print(Celcius(a))

#------------------------------------------------------------
"""
..EJEMPLO DE TRY,ELSE,FINALLY:

-Python tiene un libro con las excepciones explicadas como:ZeroDivisionError, ValueError.

* link = https://docs.python.org/3/library/exceptions.html#base-classes
"""
try:
    a= input("Digite una valor: ")
    b= input("Digite una valor: ")
    resultado = int(a)/int(b)
    print(resultado)
except(ValueError,ZeroDivisionError): #Aqui indicamos que si hay 
    #alguno de esto 2 errores, ejecute el print de abajo.
    print("Hay un error pendejo!")
    
else:
    print("Es posible elevar al cuadrado, pero no dividir")        
      
finally:
    print("Gracias por usar el codigo.")