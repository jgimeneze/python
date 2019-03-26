# -*- coding: utf-8 -*-
# Requiere tkinter instalado:   # dnf install python3-tkinter

########################################################################
#                               IMPORT
########################################################################
from tkinter import *
from tkinter import ttk


########################################################################
#                   VARIABLES GLOBALES Y CONSTANTES
########################################################################


########################################################################
#                               NIVEL 2
########################################################################


########################################################################
#                               NIVEL 1
########################################################################

#######################  FUNCIONES DESDE TKINTER  ######################
def incremento(inc):
    contador = int(str(resultado['text']))
    contador = contador + inc
    resultado.config(text=str(contador))

###############################  MAIN  #################################

if __name__ == "__main__":

	# Definimos la ventana
	ventana = Tk()
	ventana.title("Super útil")
	ventana.geometry('350x200')

	# Definimos los elementos de la ventana
	resultado = Label(ventana, text="0", fg="grey", bg="#BCED34", font=("Comic sans", 16))
	 
	boton_incremento = Button(ventana, text="Incrementar en 1", command=lambda: incremento(1))

	# Mostramos los elementos de la ventana
	boton_incremento.pack(side=LEFT, fill=BOTH, expand=True, pad=10, pady=10)
	resultado.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)

	# Bucle de la ventana
	ventana.mainloop()
