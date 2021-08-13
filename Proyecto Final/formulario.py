#Formulario Omind Sex
#Limpiamos pantalla
import os  
os.system("cls")
 
from tkinter import *
#Modulo que permite imprimir el texto en colores
from colorama import Fore, init
init()

def send_data():
#Definición de las variables
  usuario_info = usuario.get()
  contraseña_info = contraseña.get()
  nombre_info = nombre.get()
  edad_info = str(edad.get())

#Crearemos nuestra base de datos 
  file = open("registro.txt", "a")
  
#Guardamos la información solicitada 
  file.write(usuario_info)
  file.write("\t")
  file.write(contraseña_info)
  file.write("\t")
  file.write(nombre_info)
  file.write("\t")
  file.write(edad_info)
  file.write("\t\n")
  file.close()
  print(Fore.RED + "Usuario registrado | Bienvenido a Omind Sex")
  
 #Borrar información despues de guardarla 
  usuario_entry.delete(0, END)
  contraseña_entry.delete(0, END)
  nombre_entry.delete(0, END)
  edad_entry.delete(0, END)

#Diseño del encabezado 
mywindow = Tk()
mywindow.geometry("650x550")
mywindow.title("REGISTRO OMIND SEX ")
mywindow.resizable(False,False)
mywindow.config(background = "#fa8bf1")
main_title = Label(text = "REGISTRO | OMIND SEX", font = ("calibri", 16), bg = "#fa8bf1", fg = "white", width = "500", height = "2")
main_title.pack()

#Diseño y posición del texto solicitando la información
usuario_label = Label(text = "Usuario", bg = "#fa8bf1", fg = "white", font = ("calibri", 14))
usuario_label.place(x = 200, y = 100)
contraseña_label = Label(text = "Contraseña", bg = "#fa8bf1", fg = "white", font = ("calibri", 14))
contraseña_label.place(x = 200, y = 160)
nombre_label = Label(text = "Nombre completo", bg = "#fa8bf1", fg = "white",font = ("calibri", 14))
nombre_label.place(x = 200, y = 220)
edad_label = Label(text = "Edad", bg = "#fa8bf1", fg = "white", font = ("calibri", 14))
edad_label.place(x = 200, y = 280)
 
'''
Definición de variables de control: 
objetos especiales que se asocian a los widgets para almacenar sus valores 
y facilitar su disponibilidad en otras partes del programa
'''
usuario= StringVar()
contraseña = StringVar()
nombre= StringVar()
edad= StringVar()

 #Creamos las entradas para que el usuario pueda llenar el formulario 
usuario_entry = Entry(textvariable = usuario, width = "40")
contraseña_entry = Entry(textvariable = contraseña, width = "40",  show = "*") #Mostramos * para seguridad al crear contraseña
nombre_entry = Entry(textvariable = nombre, width = "40")
edad_entry = Entry(textvariable = edad, width = "40")
 
#Posicionamos las entradas de texto 
usuario_entry.place(x = 200, y = 130)
contraseña_entry.place(x = 200, y = 190)
nombre_entry.place(x = 200, y = 250)
edad_entry.place(x = 200, y = 310)
 
#Diseño botón de registro 
submit_btn = Button(mywindow,text = "Registrarse", width = "30", height = "2", command = send_data, bg = "#fc6998", font = ("calibri", 12))
submit_btn.place(x = 210, y = 350)

mywindow.mainloop()