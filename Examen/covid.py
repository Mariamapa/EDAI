#Medidor de covid 
import pandas as pd
import numpy as np
#Limpiamos pantalla 
import os 
os.system("cls")
#Modulo que permite imprimir el texto en colores 
from colorama import Fore, init
init()
#Se definen variables 
op='0'
datos=[]
inf=0
prom=0
#Damos mensaje de bienvenida 
print("\n\t\t\t\tBienvenido al indicador de covid \n\n\n\n")
while(op!='2'):
	print('\n')
	print(" 1)Llenar\n 2)Salir") #Abrimos un menú para la selección 
	op=input("Elige una opción: ")
	if op=='1':
        #Solicitamos información 
		edad=input("Edad del paciente: ") 
		rango=input("Rango obtenido en estudio [0-1]: ")
        #Se da el rango para dividir a la población con casos positivos y casos negativos.
		if float(rango)>=0.8:
			inf=inf+1
			prom=prom+int(edad)
		reg=edad+','+rango+'\n'
		datos.append(reg)
	elif op=='2':
		print("Vuelva pronto")
	else:
		print("Opción no valida")
a=open("bd.csv","a")
a.writelines(datos)
a.close()
prom=prom+int(edad)

#Mostramos el color del semaforo 
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
        
a=open("bd.csv","r")
infor=a.read()
a.read()  
a.close()
prom=prom/inf 
print("Edad promedio de los infectados ",prom)