import csv
from BACKEND import *
def menu():

    paises = []

    try:
        archivo = open(ARCHIVO, "r", encoding="utf-8")

        lector = csv.DictReader(archivo)

        for fila in lector:

            pais = {
                "nombre": fila["nombre"],
                "poblacion": int(fila["poblacion"]),
                "superficie": int(fila["superficie"]),
                "continente": fila["continente"]
            }

            paises.append(pais)

        archivo.close()

    except FileNotFoundError:
        print("No se encontró el archivo.")

    while True:

        print("\n====== MENÚ ======")
        print("1- Mostrar países")
        print("2- Agregar país")
        print("3- Actualizar país")
        print("4- Buscar país")
        print("5- Filtrar por continente")
        print("6- Filtrar por población")
        print("7- Filtrar por superficie")
        print("8- Ordenar")
        print("9- Estadísticas")
        print("0- Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            mostrar(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais(paises)

        elif opcion == "5":
            filtrar_continente(paises)

        elif opcion == "6":
            filtrar_poblacion(paises)

        elif opcion == "7":
            filtrar_superficie(paises)

        elif opcion == "8":
            ordenar(paises)

        elif opcion == "9":
            estadisticas(paises)

        elif opcion == "0":
            print("Fin del programa.")
            break

        else:
            print("Opción inválida.")


menu()
