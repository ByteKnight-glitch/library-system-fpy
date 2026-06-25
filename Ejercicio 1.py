from menu import leer_opcion, mostrar_menu
from funciones import (
	agregar_libro,
	actualizar_disponibilidad,
	buscar_libro,
	eliminar_libro,
	mostrar_libros,
)


def main():
	lista_libros = []

	while True:
		mostrar_menu()
		opcion = leer_opcion()

		if opcion == 1:
			agregar_libro(lista_libros)
		elif opcion == 2:
			titulo = input("Ingrese el titulo del libro a buscar: ")
			posicion = buscar_libro(lista_libros, titulo)

			if posicion == -1:
				print(f"El libro '{titulo}' no se encuentra registrado.")
			else:
				actualizar_disponibilidad(lista_libros)
				print(f"El libro se encuentra en la posicion {posicion}.")
				mostrar_libros(lista_libros, posicion)
		elif opcion == 3:
			eliminar_libro(lista_libros)
		elif opcion == 4:
			actualizar_disponibilidad(lista_libros)
			print("Disponibilidad actualizada.")
		elif opcion == 5:
			mostrar_libros(lista_libros)
		elif opcion == 6:
			print("Gracias por usar el sistema. Vuelva Pronto")
			break


if __name__ == "__main__":
	main()
