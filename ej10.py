#SUPER HARD, vale 10 puntos para Griffindor: Escribir un piedra, papel o tijera de 1 ronda.
#http://www.pythondiario.com/2013/11/piedra-papel-o-tijera-juego-en-python.html
import random
from time import sleep

print "****** Piedra, papel o tijera (3 intentos) ******"
print ""
sleep(2)

# Inicio
 x = 0
 tu = 0
 pc = 0
 
 while str(x) != 3:
  
  ingresoOpcion = false
  while ingresoOpcion == false
    print "Piedra (1), papel (2) o tijera (3)?"
    opcion = raw_input()
    if opcion != 1 and opcion != 2 and opcion != 3:
        ingresoOpcion = false
    else:
        ingresoOpcion = true
    
  
  
  
  azar = random.choice(["piedra", "papel", "tijera"])
  if opcion == azar:
   print "El pc tambien elijio", azar
   print ""
  elif azar == "tijera" and opcion == "papel":
   x += 1
   pc += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "tijera" and opcion == "piedra":
   x += 1
   tu += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "piedra" and opcion == "tijera":
   x += 1
   pc += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "piedra" and opcion == "papel":
   x += 1
   tu += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "papel" and opcion == "tijera":
   x += 1
   tu += 1
   print "El PC saco", azar
   print "Tu", tu, "PC", pc
   print ""
  elif azar == "papel" and opcion == "piedra":
   x += 1
   pc += 1
   print "El pc saco", azar
   print "Tu", tu, "PC", pc
   print ""
  else:
   print "Opcion incorrecta, vuleva a intentarlo"
 
 print ""
 
 if pc > tu:
  print "Gano el PC", pc, "a", tu
 elif pc == tu:
  print "Empataron", tu, "a", pc
 else:
  print "Ganaste", tu, "a", pc
 
 print ""
 print "PARTIDA TERMINADA"
