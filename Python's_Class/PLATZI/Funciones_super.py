# Imprime los número impares de una lista con varios metodos.


# Usando List comprehension
# my_list =[1, 4, 5, 6, 9, 13, 19, 21]
# new_list=[i for i in my_list if i % 2 !=0]
# print(new_list)

# Usando filter
# my_list =[1, 4, 5, 6, 9, 13, 19, 21]
# new_list = list(filter(lambda x :x % 2 != 0, my_list))
# print(new_list)

#Imprima el cuadrado de los siguientes número de la lista
#Usando List comprehension
# my_list = [1,2,3,4,5]
# square =   [i **2 for i in my_list]
# print(square)

# #Usando map
# my_list =[1, 2, 3, 4, 5]
# square = list(map(lambda x :x**2, my_list))
# print(square)

#Multiplique los números de la lista entre ellos

from functools import reduce
my_list =[2, 2, 2, 2, 2]
all_multiplied= reduce(lambda a, b: a*b, my_list)
print(all_multiplied)
