from tkinter import *   

root= Tk()
root.title("Ejemplo")
foto =PhotoImage(file="84316.png")
Label(root, image=foto).pack()

movie1=IntVar()
movie2=IntVar()
movie3=IntVar()



def option():
    opcion_escogida=""
    if (movie1.get()== 1):
        opcion_escogida+="La mejor pelicula"
    if (movie2.get()== 1):
        opcion_escogida+="Buena opción"
    if (movie3.get()== 1):
        opcion_escogida+="Pudo ser mejor pelicula"
        
    textofinal.config(text=opcion_escogida)    

frame=Frame(root)
frame.pack()
Label(frame, text="Elige una pelicula: ", width=50).pack()

Checkbutton(frame,text="Lord of rings",variable=movie1,onvalue=1,offvalue=0,command=option).pack()
Checkbutton(frame,text="Hobbit",variable=movie2,onvalue=1,offvalue=0,command=option).pack()
Checkbutton(frame,text="The return of the king",variable=movie3,onvalue=1,offvalue=0,command=option).pack()

textofinal=Label(frame) #--Label para mostrar mensaje según la opcion elegida.
textofinal.pack()

root.mainloop()