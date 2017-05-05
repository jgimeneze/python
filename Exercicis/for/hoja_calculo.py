# coding:utf-8

def my_range(inici, fi, increment):
	while inici <= fi:
		#Retorna l'element actual del rang (llista)
		yield inici
		inici = inici + increment


for fil in my_range(1, 5, 1):
	for col in my_range(1, 4, 1):
		# La fila 1 tiene un tratamiento especial
		if ( fil==1 ):
			if ( col==2 ):
				print "A",
			elif  ( col==3 ):
				print "B",
			elif  ( col==4 ):
				print "C",
			else:
				print "-",
		else:
			# La fila es <> de la 1
			# Si es la primera columna ponemos
			# el numero de orden
			if ( col==1 ):
				print fil-1 ,
			else:
				# Ponemos los * por coordenadas
				if ( ( fil==3 and col==3 ) or
				     ( fil==4 and col==2 ) ):
					print "*",
				# Caso general ponemos -
				else:
					print "-",

	print ""  # Hace un INTRO al acabar la fila

