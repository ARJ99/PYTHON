""" Ejercicio :La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

- Ingredientes vegetarianos: Pimiento y tofu.
- Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

Pizzeria = """Bienvenido a la Pizzería \"Bella Napoli\"

Elija el tipo de pizza que deseas :

1- Vegetariana
2- Tradicional

"""
Vegetariana = ["S. Tomate, Masa Artesanal"]

Tradicional =["S. Tomate, Masa Artesanal, Mozzarella"]

Pizza = int(input(Pizzeria))

if Pizza == 1:
    ingredientes1 =int(input("""Has elegido un piza Vegetaria, Los ingrendientes para su pizza son : Pimiento, Tofu,S. Tomate y Masa Artesanal. Selecciona un ingrediente principal entre el Pimiento y el Tofu

    1- Pimiento
    2- Tofu
    
    """))
    
    if ingredientes1 == 1:
        
      Vegetariana.append("Pimiento")
      print("Has elejido Pimiento")
      print("Tú pizza Vegetariana tiene los siguientes ingredientes :{}".format(Vegetariana))
    else:
        Vegetariana= Vegetariana.append("Tofu")
        print("Has elejigo Tofu")
        print("Tú pizza Vegetariana tiene los siguientes ingredientes :{}".format(Vegetariana))
else:
     ingredientes2  =int(input(""" Has elegido una pizza Tradicional, Los ingredientes para su pizza son: Peperoni, Jamón, Salmón, S.Tomate y Masa Artesanal. Selecciona un ingrediente principal entre el Peperoni, Jamón y Salmón

     1- Pepperoni
     2- Jamón
     3- Salmón

     """)) 
     if ingredientes2 ==1:
        Tradicional.append("Pepperoni")
        print("Has elegido Peperoni")
        print("Tú pizza Tradicional tiene los siguientes ingredientes : {}".format(Tradicional))
     elif ingredientes2 ==2:
        Tradicional.append("Jamón")
        print("Has elegido Jamón")
        print("Tú pizza Tradicional tiene los siguientes ingredientes : {}".format(Tradicional))
     else:
        Tradicional.append("Salmón")
        print("Has elegido Salmón")
        print("Tú pizza Tradicional tiene los siguientes ingredientes : {}".format(Tradicional))   

        





