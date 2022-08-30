## Ejercicio: Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

Amount = float(input("Digite la cantidad de dinero a invertir : "))
Interest = float(input("Digite el interes anual : "))
Years = int(input("Digite a cuantos años deseas la inversion : "))

for i in range(Years):
    #Amount *= 1+ Interest/100
    Amount= Amount* 1 + Interest/100 # Error del codigo. Por qué?
    
   

    print("Su Capital tras "+ str(i)+" años es : "+ str(round(Amount,2)))
   

#------------------------------------------------------------
#Version correcta del ejercicio:
# amount = float(input("¿Cantidad a invertir? "))
# interest = float(input("¿Interés porcentual anual? "))
# years = int(input("¿Años?"))
# for i in range(years):
#     amount *= 1 + interest / 100 
#     print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))