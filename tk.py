from tkinter import *

main = Tk()
main.title ("Banda")
main.geometry ("117x106")
imagen = PhotoImage(file="bigblue.png")
fondo = Label(main, image=imagen).place(x=0 ,y = 0)
frame = Frame()

frame.pack() 
main.mainloop()