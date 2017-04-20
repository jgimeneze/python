# coding:utf-8
def mensaje_bienvenida(nombre, apellido1, apellido2):
	print "*****************************"
	print "          BIENVENIDO         "
	print " ", nombre , "," , apellido1, "," , apellido2
	print "*****************************"
	
	nombre="CAMBIO"
	apellido1="CAMBIAZO"
	apellido2="CAMBIAZON"
	
	return apellido1,apellido2
	
#############################################################################	

nombre_invitado="PEPE"
apellido1_invitado="SANCHEZ"
apellido2_invitado="LOPEZ"

print nombre_invitado , apellido1_invitado, apellido2_invitado


# nombre_invitado    : parámetro no modificable
# apellido1_invitado : parámetro modificable
# apellido2_invitado : parámetro modificable
apellido1_invitado,apellido2_invitado=mensaje_bienvenida(nombre_invitado,apellido1_invitado,apellido2_invitado)


# Sólo cambia el valor de los parámetro modificables
print nombre_invitado , apellido1_invitado, apellido2_invitado
