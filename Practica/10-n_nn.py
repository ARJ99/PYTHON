#Ejercicio 10: Solicitar al usuario un número n y calcular  n +nn +nnn

n =input('Digite un número')
n=int(n)
nn=int('{}{}'.format(n, n))
nnn=int('{}{}{}'.format(n, n, n))


outcome= n + nn+ nnn
print(outcome)

