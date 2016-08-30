import random

diccionarioAlumnos = {}
diccionarioMaterias = {}
diccionarioCarrera = {}

# materias de la carrera
while(True):
	# Ingresa Nombre Carreta
	nombreMateria = input("Ingrese nombre de la Carrera: ")
	existe = True
	while (existe):
		idMateria = int(str(random.randint(1, 9)) + str(random.randint(1, 9)) + str(rand.randint(1, 9)) + str(random.randint(1, 9)) + str(random.randint(1, 9)))
	
		for clave, valor in diccionarioMaterias:
			for id, nombre in clave:
				if id == idMateria:
					existe = True
				else:
					existe = False
	
	# cargo la materia en un diccionario				
	diccionarioMaterias[idMateria] = nombreMateria
	
	# cargo la materia del alumnos
	diccionarioAlumnos["materia"] = nombreMateria
	
	# Ingreso los alumnos en una lista
	while(True):
	    # valido los caracteres del nombre
	    while(True):
	        nombreAlumno = input("Ingrese nombre del alumno: ")
	        if len(nombreAlumno) < 5:
	            print("El nombre debera contener 5 caracteres como minimo.")
	        else:
	            break
	    # valido la longitud de la nota
	    while(True):
	        notaAlumno = float(input("Ingrese la nota del alumno: "))
	        if (notaAlumno >= 0 and notaAlumno <= 10) == False:
	            print("La nota debe estar entre 0 y 10.")
	        else:
	            break
	    # asigno el alumno al diccionario
	    diccionarioAlumnos[nombreAlumno] = notaAlumno
	    
	    # pregunto si desea continuar
	    print(" ")
	    rta = input("Desea cargar mas alumnos? (y/n)")
	    print(" ")
	    if rta != "y":
	        print(" ")
	        break
		
		# cargo la materia en un diccionario				
		diccionarioMaterias[idMateria] = diccionarioAlumnos
	
		diccionarioCarrera[idMateria] = diccionarioMaterias
	
	# pregunto si desea continuar cargando materias
	print(" ")
	rta = input("Desea cargar mas alumnos? (y/n)")
	print(" ")
	if rta != "y":
	    print(" ")
	    break
