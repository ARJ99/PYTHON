#cars = ["Ford","BMW","Volvo","1","3"]

"""
1)
list.sort()  Organiza alfabeticamente los elementos de la lista.
primero numeros y luego letras. orden acentente.

2)
list.sort(reverse = True) Organiza en orden Decendente, letra luego números.

"""
#1)
#cars.sort()

#2)
# cars.sort(reverse = True)
#print(cars)

#--------------------------------------------------------------
def myFunc(e):
  return e['year']
#Organiza la lista-diccionario con una función y usando el year del valor de los diccionarios. 
cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)
print(cars)
