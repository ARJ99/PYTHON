#Ejercicio 4: Solicitar el valor del radio de un circulo y hallar su área.

#La libreria math se  usó para obtener el valor de pi y para el round del resultado

from math import pi
import math

r= float(input('Escriba el radio del circulo'))

area= pi*r**2
redondeo = round(area, 2)



#print('El área del circulo es {}'.format(redondeo))
print('El área para un circulo con un radio de {}  es: {}'.format(r,redondeo))
