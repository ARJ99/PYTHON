#El Datetime es el modulo principal.
import datetime

# #..Display the current date
x = datetime.datetime.now()
print(x)

print(x.year)
print(x.hour)
print(x.minute)
print(x.second)
print(x.day)

#-------------------------------------------------------------
#..Desde el modulo Datetime solo traeremos date para mostrar fecha.

from datetime import date

# The date module represents a date in the format YYYY-MM-DD.
# Constructor of this class needs three mandatory arguments year, 
# month and date.

#..Ejemplo:
my_date = date(1999, 4, 14)
print("This is my birthday: ",my_date)
#-------------------------------------------------------------
#..The strftime() Method

#.. Link con metodos strtime : https://www.w3schools.com/python/python_datetime.asp

#..Example : Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) #-- Month's name

print(x.strftime("%A")) #-- Weekday

print(x.strftime("%d")) #-- Day of month 01-31

print(x.strftime("%I %p")) #- Hour 00-12 y el otro es AM O PM

#-------------------------------------------------------------
