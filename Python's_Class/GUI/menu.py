
from tkinter import *
from tkinter import messagebox


root = Tk()
root.title("Ejemplo")

def infoAdicional():
    messagebox.showinfo("Procesador de Alejandro","Primera prueba") #-Esta syntax y el modulo messagebox son necesarios para que funcione la venta emergente.

def avisolicencia():
    messagebox.showwarning("Licencia","Producto bajo licencia GNU")
    
def saliraplicacion(): #-Funcion para cerrar ventana o aplicación.
    
    #..Cerrar venta con botones SI o No
    # valor=messagebox.askquestion("Salir","Deseas salir de la app? ")  
    # if valor =="yes":  #-Valor ofrece los botones si("yes") y no(not)
    #     root.destroy()
    
    
    #..Cerrar venta con botones ACEPTAR O CANCELAR
    valor=messagebox.askokcancel("SALIR","Estas seguro que quieres cerrar")
    if valor == True:
        root.destroy()
        
def cerrardocumento():
    valor=messagebox.askretrycancel("Reintentar","No es posible abrir Doc.")        
          

BarraMenu= Menu(root)
root.config(menu=BarraMenu,width=300,height=300)#-Creación del menú principal

#*EL tearoff =0 Sirve para eliminar el ---- por default que tiene el menú.
archivo_menu=Menu(BarraMenu,tearoff=0)#-Seccion que será asignada al menu principal.
archivo_menu.add_command(label="Nuevo") #-Metodo para agregar opciones desplegables en el menú.
archivo_menu.add_command(label="Guardar")
archivo_menu.add_command(label="Guardar Como")
archivo_menu.add_separator()#-Metodo sirve para separar horizontalmente con linea por grupos.
archivo_menu.add_command(label="Cerrar",command=cerrardocumento)
archivo_menu.add_command(label="Salir",command=saliraplicacion)

archivo_edicion=Menu(BarraMenu,tearoff=0)
archivo_edicion.add_command(label="Copiar")
archivo_edicion.add_command(label="Cortar")
archivo_edicion.add_command(label="Pegar")

archivo_herramientas=Menu(BarraMenu,tearoff=0)

archivo_ayuda=Menu(BarraMenu,tearoff=0)
archivo_ayuda.add_command(label="Licencia", command=avisolicencia)
archivo_ayuda.add_command(label="Acerca de",command=infoAdicional)

BarraMenu.add_cascade(label="Archivo",menu=archivo_menu)#-El metodo add_cascade sirve para darle texto a cada seccion del menú.
BarraMenu.add_cascade(label="Edición",menu=archivo_edicion)
BarraMenu.add_cascade(label="Herramientas",menu=archivo_herramientas)
BarraMenu.add_cascade(label="Ayuda",menu=archivo_ayuda)


root.mainloop()