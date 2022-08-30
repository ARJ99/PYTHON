"""#..  Python RegEx:
#*   Link patrones de busqueda: https://www.w3schools.com/python/python_regex.asp

A RegEx, or Regular Expression, is a sequence of characters that forms
a search pattern.

RegEx can be used to check if a string contains the specified search 
pattern. 

#..Ejemplo: (Importamos el modulo RegEx) -Search the string to see if 
# ..it starts with "The" and ends with "Spain":

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
"""
#-------------------------------------------------------------------

#..MODULE RegEx
import re

"""
#.. The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
"""
#..Ejemplo:

# txt = "When I saw your eyes"

# x = re.search(r"When",txt)
# if x:
#     print("Yes, We have a match!")
# else:
#     print("No match.")  


#--------------------------------------------------------------------
"""
#.. The findall() Function
The findall() function returns a list containing all matches.

"La r indica una expresion regular para buscar y no un salto de pagian \n."

#- Syntax
re.findall(string,iterable)

"""
#..Ejemplo:
""" Buscar 2 carateres cualquiera y la letra L
. =	Any character """

# frase = "Saludos a todos desde Bucaramanga."
# check = re.findall(r"..l",frase)
# print(check)

# #..Ejemplo:
"""Buscar el 2 from list."""
# list =str([2, 4, 2, 5, 6, 6])

# show = re.findall(r"2",list)
# print(show)    
#--------------------------------------------------------------------  
#..The split() Function
"""The split() function returns a list where the string has been split at each match:"""

#..Example:
"""Split at each white-space character:"""

import re

# txt = "The rain in Spain"
# x = re.split("\s", txt)
# print(x)  
#--------------------------------------------------------------------  
#..The sub() Function
"""The sub() function replaces the matches with the text of your choice:

#.. Example:
Replace every white-space character with the number 9:"""

import re

# txt = "The rain in Spain"
# x = re.sub("\s", "9", txt)
# print(x)

#------------------------------------------------------------------
#..Set of Examples to prove the previous methods.

#..Examples: re.search()

# txt = "I realized that how much happy you can be with the correct person."

# result = re.search(r"Z",txt)
# if result :
#     print("We have match")
# else:
#     print("No match.")  

#..Examples: re.search()

# txt1 = "I agree with js"

# result = re.search("^I.*js$",txt1)
# if result :
#     print("We have match")
# else:
#     print("No match.")  

#..Examples: re.findall()
# """El uso de | es igual a OR """

# txt2 = "hello world, well done"

# result = re.findall(".e...|done",txt2)
# print(result) 

#..Examples: re.findall()
"""Search for a sequence that starts with "pep", followed excactly 3
(any) characters:"""

txt3 = "pepsis peperoni pica a pepito"

result1 = re.findall("pep.{3}",txt3)
print(result1) 
result2 = re.findall("pep.?",txt3)
print(result2) 
     