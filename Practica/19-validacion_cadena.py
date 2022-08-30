# Ejercicio 19 : Comprobar is una cadena termina con la extensión .py, si no es así, agregar la extensión.

def MainString(documento):
    extension_correcta = ".py"
    desglozar =documento.split(".")
    extension=desglozar[-1]
    nueva_extension= desglozar[0]

    if extension == extension_correcta :
        print( "El formato es valido.")
    else:
        return nueva_extension + ".py"

print(MainString("trabajo.py"))
    
 