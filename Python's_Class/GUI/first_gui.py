from cgitb import text
import string
from tkinter import * #.. Modulo Tkinter para crear GUI
from turtle import left 

#..Creacion de Raiz
raiz = Tk()   #--Tk: es la raíz de la interfaz,
#--donde vamos a colocar el resto de widgets.

"""
#.. Si deseas ejecutar el archivo como aplicación sin tener que abrir la consola. Solo debes cambiar la extension del archivo que contiene el modulo con el codigo por .pyw y se ejecutara como una aplicación.

"""

raiz.title("Ventana Emergente") #--Editar nombre de ventana.

raiz.iconbitmap("halo.ico") #--Icono de la ventana. El Archivo ico, debe estar en la carpeta que contiene el modulo del codigo.
raiz.resizable(True,True) #-- Metodo para dejar a un tamaño especifico la raiz.
#raiz.geometry("650x350") #--Metodo para definir el tamaño weidht or hight de la pestaña.

raiz.config(bg = "orange") #--Editar el color del fondo de pantalla raiz. Nombre en ingles del color.
#* Configuraciones adicionales para el ROOT 
raiz.config(cursor="hand1")
raiz.config(relief="flat")
#raiz.config(bd=35) #-- Configuración del borde
#---------------------------------
#..Creacion de Frame

my_frame= Frame()
my_frame.pack()  #--El frame debe empaquetarse dentro de la raiz.
#my_frame.pack(side="right",anchor ="s") 

 # You can choose the side to pack the frame.(left,top,bottom)
 #if you put in the anchor method the first word or North,South,East,West. you can address the frame.

my_frame.config(bg="#6495ED") #--Para ver el frame debemos darle color de fondo.
#--------------------------------
#..Expandir Frame Horizontalmente o Verticalmente (Packer Options)

#my_frame.pack(fill="x")
my_frame.pack(fill="both", expand="True") #-Puedes elegir x, y o both como parametros para expandir.

my_frame.config(width ="650", height = "350") #--Para ver el frame debemos darle tamaño."La raiz siempre se adapta al tamaño de su frame." 
#*Debes darle tamañao al frame y no a la raiz.
#--------------------------------
#..Cambiar el borde del frame.

"""#* Relief style flat,groove,raised,ridge,solid or sunken"""
my_frame.config(relief="flat")
my_frame.config(bd=35)

#.. Cambiar el cursor

my_frame.config(cursor="hand2") #--Solo escribes el tipo de cursor.

#---------------------------------
#.. Creacion de Label para texto
#texto = Label(my_frame, text="HI THERE! HOW ARE YOU DOING?",font=("Times",20))
#texto.place(x=80, y =50) #-- El metodo place sirve para empaquetar tambien.
#---------------------------------
#..Poner Imagenes ( Solo PGN ó GIFT)
#my_image=PhotoImage(file="84316.png") #- La foto debe estar en la carpeta del archivo first_gui.py
#Label(my_frame, image=my_image).place(x=50, y = 100)
#---------------------------------
#.. Creacion Cuadro de texto.

#-Se puede usar este metodo para colocar cuadros de  texto
#cuadrotexto =Entry(my_frame)
#cuadrotexto.place(x=250, y = 120)

#-La mejor forma es usar el metodo grid() Es una cuadricula

#* Primer casilla de texto para digitar el Nombre
texto1=Label(my_frame,text="Nombre :") #------------------------Crear el texto para la casilla.
texto1.grid(row=0, column=0, sticky="e",padx=10, pady =10) #------Ubicación de texto por metodo grid.
texto1.config(relief="ridge",bd=5) #--------------------------------Define el estilo y grosor del borde.
cuad_texto1 =Entry(my_frame)  #---------------------------------------Cuadro de texto.
cuad_texto1.grid(row=0,column=1) #--------------------------------------Ubicación de texto por metodo grid.
cuad_texto1.config(relief="sunken",bd=5, justify="center") #--------------------------------Define el estilo y grosor del borde.


#* Segunda casilla de texto para digitar el Apellido
texto2 = Label(my_frame, text="Apellido:")
texto2.grid(row=1, column=0, sticky="e",padx=10, pady =10)
texto2.config(relief="ridge",bd=5)
cuad_texto2 =Entry(my_frame)
cuad_texto2.grid(row=1,column=1)
cuad_texto2.config(relief="sunken",bd=5,justify="center") #--- Justify orienta el texto dentro del cuadro de texto.

#* Tercera casilla de texto para digitar el Password
texto3 = Label(my_frame, text="Password:")
texto3.grid(row=2, column=0,sticky ="ne",padx=10, pady =10)
texto3.config(relief="ridge",bd=5)
cuad_texto3 =Entry(my_frame)
cuad_texto3.grid(row=2,column=1)
cuad_texto3.config(relief="sunken",bd = 5,justify="center")
cuad_texto3.config(show="*") #-Metodo para ocultar lo que escribes para una password.

#* Cuarta casilla de texto para digitar el Password
texto4 = Label(my_frame, text="Comentario:")
texto4.grid(row=3, column=0, sticky="e",padx=10, pady =10)
texto4.config(relief="ridge",bd=5)

Coment1=Text(my_frame,width=50,height=10) #--------Creamos Cuadro de texto grande para coments.
Coment1.grid(row=3,column=1,padx=10, pady =10)
Coment1.config(font=("Times",10))
scrollvert=Scrollbar(my_frame,command= Coment1.yview) #--Crear un scrollbar
#-el commando metodo nos indica a que widget pertenece el scrollbar,
scrollvert.grid(row=3, column=2,sticky="nsew") #--Con sticky logramos que el scrollbar se adapte al tamaño de lo que escribas.
Coment1.config(yscrollcommand=scrollvert.set) #-- Indica en que lugar el texto se encuentra el scrollbar.

#---------------------------------
#..Crear Buttom y funcion al buttom

#-El codigo del buttom debe estar por encima del codigo de cuadro de texto.

myname=StringVar()
def codigoboton():
    myname.set("ERES GENIAL") #-Definir un valor por default con set
    
Bottom1 =Button(my_frame, text="Enviar",command=codigoboton,activebackground="#FF7F50")#--El activebackground sirve para cambiar el color de un buttom si esta precionado.
Bottom1.place(x=150,y=350)  #-Metodo para ubicar el bottom en una espacio determinado.

#* codigo de cuadro de texto para ejemplo del Buttom

cuadro_text0=Entry(my_frame, textvariable=myname) #-El metodo textvariable sirve para asignar un texto al cuadro de texto.
cuadro_text0.grid(row = 4, column =1,padx=10, pady =10)#-El padx y pady son los espacios que tendra de margen.

#---------------------------------
#..Creacion de RadioButtom
R_buttom0 = Radiobutton(my_frame, text="Masculino").place(x=100, y= 390)
R_buttom1= Radiobutton(my_frame, text="Femenino").place(x=100, y = 450)

#---------------------------------
raiz.mainloop()  #-- Es un bucle infinito para mostar la ventatana
"""".. El mentodo mainloop siempre debe ir al final"""



