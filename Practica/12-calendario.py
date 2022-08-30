#Ejercicio 12: Imprimir el calendario para un año y mes especifico
import calendar

año= int(input('Escriba el año:'))
mes= int(input('Escriba el mes:'))
print(calendar.month(año,mes))