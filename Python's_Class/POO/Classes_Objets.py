"""#.. Programación orientada a objetos.
Es una paradigma de programación en el cual usamos objetos y sus interacciones para el desarrollo.

Un objeto: tiene caractericas(atributos) y puede realizar acciones(metodos)

clase: Es un contenedor que sirve de pantilla en el cual establecemos los atributos y metodos del objeto.

Encapsulación =  Es el principio que asegura que una clase controle especificamente los atributos y metodos para
interacturar, de ese modo solo la misma clase podra modificar el objeto. 

Abstracción = Son las características especificas de un objeto(Atributos y Metodos), aquellas que lo distinguen de los
demás tipos de objetos.

Herencia = Se puedan definir nuevas clases basadas de unas ya existentes, a fin de reutilizar el código, generando así 
una jerarquía de clases dentro de una aplicación. Si una clase deriva de otra, esta hereda sus atributos y métodos y 
puede añadir nuevos atributos, métodos o redefinir los heredados.

Polimosfismo = Se refiere a la posibilidad de definir clases diferentes que tienen métodos o atributos denominados de
forma idéntica, pero que se comportan de manera distinta.

"""

"""#* The built-in __init__ (): Es usado como un constructor para crear una instancia y se requiere para poder crear objeto.

El self es usado para referenciar el objeto creado de la clase y acceder a ellas.
#----------------------------------------------------------------------------------------
#.. Python Inheritance

#- Parent class: is the class being inherited from, also called base class.

#- Child class: is the class that inherits from another class, also called derived class.

#..Create a Parent Class

class Person:
  def __init__(self, fname, lname): #--Method used to create an object.
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe") #--Here, it was created the x object, given 2 argmts.
x.printname()

#----------------------------------------------------------------------------------------

#.. Create a Child Class
"" To create a class that inherits the functionality( methods and propeties) from another class, send the parent class as a parameter when creating the child class:

class Student(Person):
  pass
  
""
#----------------------------------------------------------------------
#..Add the __init__() Function
#-When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

class Student(Person):
  def __init__(self, fname, lname):
    #add properties etc.
    
    
#-To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)    

#----------------------------------------------------------------------

#..Use the super() Function

By using the super() function, you do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)

#----------------------------------------------------------------------




#-Modificar Objetc Properties:

nombre_objeto.atributo = 40

#-Delete Object Properties:

del nombre_objeto.atributo

#-Delete Object:

del nomebre_objeto


  """
#----------------------------------------------------------
#..Ejemplo:
# class coche:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo= modelo
#         self.arrancado= False

#     def arrancar(self):
#         self.arrancado = True
#         print("El", self.marca, self.modelo, " ha arrancado.") 

#     def parar(self):
#         self.arrancado = False   
#         print("El", self.marca, self.modelo, " ha parado.")     

# laguna= coche("Renault","Model 4")
# # print(type(laguna))  # Muestra que dato es una clase
# # print(laguna.marca,laguna.modelo) # Con . accedes a los atributos del objeto.

# laguna.arrancar()
# print(laguna.arrancado)

# laguna.parar()
# print(laguna.arrancado)

#---------------------------------------------------------

#..Ejemplo: 
# Realizar un programa que  conste de una clase llamada Alumno que tenga como atributos nombre y nota.
#Inicializar sus atributos, imprimirlos y mostrar un mensaje con la nota y si aprobo el estudiante o no.

class Alumno:
    #Inicializamor atributos
    def __init__(self,nombre, nota):
        self.nombre= nombre
        self.nota= nota

    def imprimir(self):
        print("Alumno:", self.nombre)
        print("Nota: ", self.nota)

    def mostrar(self):
        if self.nota < 5:
            print("El estudiante ", self.nombre," Ha reprobado.")  
            print("Nota: ", self.nota)  
        else:
            print("El estudiante ", self.nombre," ha reprobado.") 
            print("Nota: ", self.nota)  

alumno1= Alumno("Alejandro", 5)             
alumno2= Alumno("Luis", 1)   

alumno1.imprimir()
alumno2.imprimir()

alumno1.mostrar()
alumno2.mostrar()














        