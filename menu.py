def mostrar_menu():
	print("========== MENU PRINCIPAL ==========")
	print("1. Agregar libro")
	print("2. Buscar libro")
	print("3. Eliminar libro")
	print("4. Actualizar disponibilidad")
	print("5. Mostrar libros")
	print("6. Salir")
	print("=====================================")


def leer_opcion():
	while True:
		try:
			opcion = int(input("Seleccione una opcion: "))
		except ValueError:
			print("Opcion invalida. Ingrese un numero del 1 al 6.")
			continue

		if 1 <= opcion <= 6:
			return opcion

		print("Opcion invalida. Ingrese un numero del 1 al 6.")