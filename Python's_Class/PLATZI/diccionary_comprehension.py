# Ejercicio: Crear un diccionario cuyas llaves sean los 
# 100 primero numeros naturales elevados al cubo y no sean divisible por 3.

def run():
    # my_dict = {}

    # for i in range(1,101):
    #     my_dict[i] = i**3

    # print(my_dict)    

    my_dict ={i: i**3 for i in range(1,101)if i % 3 !=0}

    print (my_dict)




if __name__=='__main__':
    run()