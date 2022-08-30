""" 
..What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your 
application.

..Create a Module
To create a module just save the code you want in a file with the file extension .py:

-Example
Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)
  
..Use a Module
Now we can use the module we just created, by using the import statement: 
 
-Example
Import the module named mymodule, and call the greeting function:

import mymodule

mymodule.greeting("Jonathan")

..Variables in Module
The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc)

--Example (Step 1)
Save this code in the file as mymodule.py 
*Este es el modulo
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
--Example (Step 2)
Import the module named mymodule, and access the person1 dictionary:
*Este es el codigo donde se manda a llamar.

import mymodule

a = mymodule.person1["age"]
print(a)
#------------------------------------------------------------------
..Re-naming a Module
You can create an alias when you import a module, by using the as keyword:

-Example
Create an alias for mymodule called mx:

import mymodule as mx

a = mx.person1["age"]
print(a)

#------------------------------------------------------------------
..Import From Module
You can choose to import only parts from a module, by using the from keyword.
#-Example (Step 1)
The module named mymodule has one function and one dictionary:

def greeting(name):
  print("Hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
-Example (Step 2)
!Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"]

Import only the person1 dictionary from the module:

from mymodule import person1

print (person1["age"])
"""