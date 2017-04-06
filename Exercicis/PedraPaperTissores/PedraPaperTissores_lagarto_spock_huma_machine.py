# coding:utf-8
# Possibilitats: PE, PA, TI, LA, SP
# Total 25: 5 empat, 20 guanyador
# jugador1 humà
# jugador2 machine

from random import randint

#Jugador humà
jugador1=raw_input("Possi la jugada (PE/PA/TI/LA/SP): ")

#Jugador machine
aleatori=randint(1,5)
if (aleatori==1):
	jugador2="PE"
if (aleatori==2):
	jugador2="PA"
if (aleatori==3):
	jugador2="TI"
if (aleatori==4):
	jugador2="LA"
if (aleatori==5):
	jugador2="SP"

print "La meva jugada és:" , jugador2

# Empat (5 combinacions)
if (jugador1==jugador2):
	print "Empat"
else: # 20 combinacions
	# Guanya jugador1 (10 combinacions)
	if (  (jugador1=="PE" and (jugador2=="LA" or jugador2=="TI") )
		or(jugador1=="PA" and (jugador2=="PE" or jugador2=="SP") )
		or(jugador1=="TI" and (jugador2=="PA" or jugador2=="LA") )
		or(jugador1=="LA" and (jugador2=="PA" or jugador2=="SP") )
		or(jugador1=="SP" and (jugador2=="PE" or jugador2=="TI") )
	   ):
		print "Tu guanyes!!!!!"
	else: # Guanya jugador2 (10 combinacions)
		print "Ets un .... has perdut !!!!"
