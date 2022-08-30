#Ejercicio 14 : Calcular la diferencia en dias de dos fechas.

from datetime import date

Today= date(2019, 9, 16)
Another_date= date(2023, 2, 13)

difference= Another_date-Today
print(difference)
print(difference.days)


