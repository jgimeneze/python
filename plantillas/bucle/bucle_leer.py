salir=False

# Leemos fuera del bucle la primera vez
print "Introduzca -1 para acabar"
num=input("Introduzca un numero: ")

# Condicion de salida
if ( num==-1 ):
	salir=True



while (salir==False):
	# Hacer cosas
	print num
	

	# Leemos dentro del bucle el resto de veces
	print "Introduzca -1 para acabar"
	num=input("Introduzca un numero: ")

	# Condicion de salida
	if ( num==-1 ):
		salir=True

