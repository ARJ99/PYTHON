"""Ejercicio: Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla."""


subjets = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
grade = []

for i in subjets:
    inquiry=input("Cual es tú nota en "+i+":")
    grade.append(inquiry)
for i in range(len(subjets)):
    print("En "+ subjets[i] + "  has sacado: "+ grade[i])    