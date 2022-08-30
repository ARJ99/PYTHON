#Ejercicio 21: Generar los n primero números pares positivos.

#Un número es par, si al dividir en 2  el resto es 0, podemos usar el metodo mod %.

def num_par(n=100):
    pares=[]

    contador = 0
    numero=0

    while contador < n:
        if numero % 2 ==0:
            pares.append(numero)
            contador += 1  #lleva el conteo para no pasarse de 100

        numero += 1 # LLeva el conteo para contar cuantos numeros pares van generados.
    return pares        

n = int(input("Escriba la cantidad de pares que desea:"))  

if n > 0:
    pares = num_par(n)
    print(pares, " Cantidad de pares:", len(pares))

else: 
    print("El número debe ser positivo.")
