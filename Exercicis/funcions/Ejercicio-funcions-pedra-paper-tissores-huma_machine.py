# coding:utf-8
############################################################################
#                        QUE HACE?
# Possibilitats: PE, PA, TI
# Total 9: 3 empat, 6 guanyador
# jugador1 humà
# jugador2 machine
############################################################################


############################################################################
#                        IMPORT
############################################################################
from random import randint


############################################################################
#                        VARIABLES GLOBALES
############################################################################
aleatori=0
jugador1=""
jugador2=""

############################################################################
#                               NIVEL 4
############################################################################
def gana_j1():
	if ( (jugador1=="PE" and jugador2=="TI") or
	     (jugador1=="PA" and jugador2=="PE") or
	     (jugador1=="TI" and jugador2=="PA") ):
		gana=True
	else:
		gana=False
		
	return gana

############################################################################
#                               NIVEL 3
############################################################################
def no_es_empate():
	# Guanya jugador1 (3 combinacions)
	if ( gana_j1() ):
		print "Tu guanyes!!!!!"
	else: # Guanya jugador2 (3 combinacions)
		print "Ets un .... has perdut !!!!"


def numero_a_jugada():
	if (aleatori==1):
		jugador2="PE"
	if (aleatori==2):
		jugador2="PA"
	if (aleatori==3):
		jugador2="TI"

############################################################################
#                               NIVEL 2
############################################################################
def jugada_j1():
	jugador1=raw_input("Possi la jugada (PE/PA/TI): ")


def jugada_machine():
	aleatori=randint(1,3)
	
	numero_a_jugada()
	
	print "La meva jugada és:" , jugador2


def resultado():
	# Empat (3 combinacions)
	if (jugador1==jugador2):
		print "Empat"
	else: # 6 combinacions
		no_es_empate()
		

	
############################################################################
#                               NIVEL 1
############################################################################
#Jugador humà
jugada_j1()


#Jugador machine
jugada_machine()


resultado()



