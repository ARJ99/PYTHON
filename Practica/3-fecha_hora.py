#Ejercicio 3: Obtener la fecha y hra actuales del sistema

# import datetime

# ahora=datetime.datetime.now()
# print(ahora)

# # La funcion strftime se usa para resetear la representacion del objeto
# print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
#-------------------------------------------------------------------------------

# Codigo para calcular años apartir de fecha de nacimiento
from datetime import date 
  
def calculateAge(birthDate): 
    days_in_year = 365.2425    
    age = int((date.today() - birthDate).days / days_in_year) 
    return age 
          
print(calculateAge(date(1999, 4, 14)), "years") 