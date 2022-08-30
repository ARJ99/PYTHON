from cgitb import text
from tkinter import *
from tkinter.tix import LabelEntry

root = Tk()
varOpcion=IntVar() #-Definimos esta variable para trabaje con la option varibel del radiobuttom.

"""
-Debes aplicar las opciones dentro del radiobuttom variable = variable_creada, value = 1
-Para que los radiobuttom solo dejen seleccionar un boton a la vez.

"""
#---------------------
#..Funciones

def imprimir():
    #print(varOpcion.get()) #-De esta forma guardamos el valor del radiobuttom selecionado.
    if varOpcion.get()==1:
        etiqueta.config(text="Has elegído Masculino.")
    else:
        etiqueta.config(text="Has elegído Femenino")    
#---------------------
Label(root,text="Selecciona el Género:").pack()
Buttom1=Radiobutton(root, text="Masculino",font=("Old Style",20),activeforeground="blue",variable=varOpcion, value=1,command=imprimir).pack()
Radiobutton(root, text="Femenino",variable=varOpcion,value=2, command=imprimir).pack()




etiqueta= Label(root)
etiqueta.pack()

#---------------------
root.mainloop()