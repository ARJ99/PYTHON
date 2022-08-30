# def run():
#     # square= []   --Punto 1 Tradicional way
#     # for i in range(1,101):
#     #     if i % 3 != 0:
#     #         square.append(i**2)

#     # print(square)       

#     square = [i**2 for i in range(1,101) if i % 3!= 0] #--List comprehension

#     print(square)
 



# if __name__=='__main__':
#     run()

# # Punto1 // Imprima el cuadrado de los numeros del 1 al 100
# #  que no sean divisibles entre 3.
#----------------------------------------------------------------------------

#-- Punto 2
#Crea una list con todos los multiplos de 4,6 y 9, hasta 5 digitos.

def run():
    chanllenge = [i for i in range(1,10000) if i % 4 ==0 and i % 6 ==0 and i % 9 ==0]
    print(chanllenge)


if __name__=='__main__':
    run()