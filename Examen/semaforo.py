#Medidor de covid 
#Limpiar pantalla 
import os 
os.system("cls")
#Libreria que nos servira para leer datos desde una base de datos 
import pandas as pd
import numpy as np
#Limpiamos pantalla 

#Modulo que permite imprimir el texto en colores 
from colorama import Fore, Back, Style, init
init()
print("\n\t\t\t\tBienvenido al indicador de covid \n\n\n\n")

#Función que leera la base de datos 
df = pd.read_csv('bd.csv')

#Definición de variables 
inf=[(df['Indicador']<0.8),(df['Indicador']>=0.8)]
res=['Negativo','Positivo']

df['Resultado']=np.select(inf,res)

inf=len(df[df['Resultado']=='Positivo'])

#Nos dara el numero de infectados y el color del semaforo 
if inf==0:
	print(Fore.GREEN + "El semaforo esta en verde, no hay infectados ")
elif inf>=1 and inf<=30:
    print("El número de infectados es",inf)
    print(Fore.YELLOW + "El semaforo esta en amarillo, Tome sus precauciones ")
elif inf>=31 and inf<=70 :
    print("El número de infectados es",inf)
    print(Back.WHITE+ Fore.RED + Style.BRIGHT + "El semaforo esta en naranja, siga las medidad de sanidad "+ Back.RESET)
elif inf>=71 and inf<=100:
    print("El número de infectados es",inf)
    print(Fore.RED + "El semaforo se encuentra en rojo, QUEDESE EN CASA ")
	#Promedio de los infectados 
print("\nEl promedio de edad de personas infectadas",df['Edad'].mean().round(0),"años.")