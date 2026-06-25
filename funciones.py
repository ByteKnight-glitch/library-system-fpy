def validar_titulo(titulo):
	return titulo.strip() != ""


def validar_copias(copias):
	try:
		valor = int(copias)
	except ValueError:
		return False

	return valor >= 0


def validar_prestamo(prestamo):
	try:
		valor = int(prestamo)
	except ValueError:
		return False

	return valor > 0


def agregar_libro(lista_libros):
	titulo = input("Ingrese el titulo del libro: ")
	if not validar_titulo(titulo):
		print("El titulo no puede estar vacio ni contener solo espacios en blanco.")
		return

	copias_texto = input("Ingrese la cantidad de copias: ")
	if not validar_copias(copias_texto):
		print("Las copias deben ser un numero entero mayor o igual que cero.")
		return

	prestamo_texto = input("Ingrese el periodo de prestamo en dias: ")
	if not validar_prestamo(prestamo_texto):
		print("El periodo de prestamo debe ser un numero entero mayor que cero.")
		return

	libro = {
		"titulo": titulo.strip(),
		"copias": int(copias_texto),
		"prestamo": int(prestamo_texto),
		"disponible": False,
	}
	lista_libros.append(libro)
	print("Libro agregado correctamente.")


def buscar_libro(lista_libros, titulo_buscar):
	titulo_buscar = titulo_buscar.strip()
	for posicion, libro in enumerate(lista_libros):
		if libro["titulo"] == titulo_buscar:
			return posicion
	return -1


def eliminar_libro(lista_libros):
	titulo = input("Ingrese el titulo del libro a eliminar: ")
	posicion = buscar_libro(lista_libros, titulo)

	if posicion == -1:
		print(f"El libro '{titulo}' no se encuentra registrado.")
		return

	del lista_libros[posicion]
	print("Libro eliminado correctamente.")


def actualizar_disponibilidad(lista_libros):
	for libro in lista_libros:
		libro["disponible"] = libro["copias"] >= 1


def mostrar_libro(libro):
	estado = "DISPONIBLE" if libro["disponible"] else "SIN COPIAS"
	print("=== LISTA DE LIBROS ===")
	print(f"Título: {libro['titulo']}")
	print(f"Copias: {libro['copias']}")
	print(f"Préstamo: {libro['prestamo']}")
	print(f"Estado: {estado}")
	print("********************************************")


def mostrar_libros(lista_libros, posicion=None):
	if posicion is not None:
		mostrar_libro(lista_libros[posicion])
		return

	actualizar_disponibilidad(lista_libros)
	print("=== LISTA DE LIBROS ===")

	if not lista_libros:
		print("No hay libros registrados.")
		return

	for libro in lista_libros:
		mostrar_libro(libro)