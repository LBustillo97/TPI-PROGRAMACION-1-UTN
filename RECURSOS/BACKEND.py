import csv

ARCHIVO = "paises.csv"



#GUARDAR DATOS

def guardar_cambios(lista): #lo usamos por ahora para guardar cambios al csv

    archivo = open(ARCHIVO, "w", encoding="utf-8")

    # Escribe el encabezado
    archivo.write("nombre,poblacion,superficie,continente\n")

    # Escribe cada país
    for pais in lista:
        linea = (
            f"{pais['nombre']},"
            f"{pais['poblacion']},"
            f"{pais['superficie']},"
            f"{pais['continente']}\n"
        )

        archivo.write(linea)

    archivo.close()


# ==========================
# MOSTRAR
# ==========================

def mostrar(lista): #con esta función mostramos la lista de países acorde a los parámetros que le demos en el momento que llamamos la función

    if len(lista) == 0:
        print("No hay datos.")
        return

    for pais in lista:
        print("-----------------------------")
        print("Nombre:", pais["nombre"])
        print("Población:", pais["poblacion"])
        print("Superficie:", pais["superficie"])
        print("Continente:", pais["continente"])


# ==========================
# AGREGAR
# ==========================

def agregar_pais(lista): #le pedimos los datos del nuevo pais al usuario, chequeando que ya no exista y que no ingrese datos inválidos, y luego llamamos a la función de guardar cambios para agregarlo al csv

    print("A continuación la pediremos los datos para agregar al nuevo país:\n")
    nombre = input("Nombre de pais: ").strip()

    if nombre == "":
        print("Nombre inválido.")
        return

    for pais in lista:
        if pais["nombre"].lower() == nombre.lower():
            print("Ese país ya existe.")
            return

    try:
        poblacion = int(input("Población: "))
        if poblacion ==0:
            raise ValueError("debe ingresar un número mayor a cero")
        superficie = int(input("Superficie: "))
        if superficie==0:
            raise ValueError("la superficie de un pais no puede ser cero")


    except:
        print("Debe ingresar números.")
        return

    continente = input("Continente: ").strip()

    if continente == "":
        print("Continente inválido.")
        return

    lista.append({
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    })

    guardar_cambios(lista)

    print("País agregado.")


# ==========================
# ACTUALIZAR
# ==========================

def actualizar_pais(lista):

    nombre = input("ingrese el país a actualizar: ").lower() #le pedimos al usuario el nombre del pais a cambiar
    no_encontrado=True

    for pais in lista:#hacemos un bucle donde revisaremos la lista de todos los paises

        if pais["nombre"].lower() == nombre.lower(): #cuando encuentre una coincidencia en la lista, entramos al IF
            no_encontrado=False
            try:
                pais["poblacion"] = int(input("ingrese la nueva población: "))
                if pais["poblacion"]==0:
                    raise ValueError("la nueva población no puede ser cero")
                pais["superficie"] = int(input("ingrese su nueva superficie: "))
                if pais["superficie"]==0:
                    raise ValueError("la nueva superficie no puede ser cero")
            except:
                print("Datos inválidos.")
                return

            guardar_cambios(lista)

            print("Datos actualizados.")
            return
    if no_encontrado==True:
        print("País no encontrado.")
        return


# ==========================
# BUSCAR
# ==========================

def buscar_pais(lista): 

    texto = input("Buscar: ").lower() #le pedimos el nombre del pais que esta buscando

    no_encontrado=True #creamos una bandera que nos ayudará a saber si encontramos una coincidencia entre lo ingresado por el usuario y la base de datos

    encontrados = [] #hacemos una variable donde copiaremos los datos del pais encontrado

    for pais in lista:

        if texto in pais["nombre"].lower():
            encontrados.append(pais)
            
            no_encontrado=False
    if no_encontrado==True:
        print("Pais no encontrado")
        return
    mostrar(encontrados)
# ==========================
# FILTROS
# ==========================

def filtrar_continente(lista):

    continente = input("ingrese el continente: ").lower()#le pedimos al usuario un continente
    if continente == "":#evitamos que el usuario ingrese vacío
        print("Error: debe ingresar un continente.")
        return
    
    no_encontrado=True #creamos una bandera que nos ayudará a saber si encontramos una coincidencia entre lo ingresado por el usuario y la base de datos
    resultado = [] #aqui guardaremos las coincidencias para después mostrarle al usuario

    for pais in lista: #hacemos un bucle que recorerrá la base de datos que importamos para encontrar coincidencias
        if pais["continente"].lower() == continente:
            resultado.append(pais)
            no_encontrado=False
    if no_encontrado==True:
        print("no se encontraron resultados para el continente escrito: ", continente)
        return
    mostrar(resultado)


def filtrar_poblacion(lista):

    try:
        minimo = int(input("Población mínima: "))
        if minimo<0:
            print("ingrese un número válido")
            return
        maximo = int(input("Población máxima: "))
        if maximo<0:
            print("ingrese un número válido")
    except:
        print("Valores incorrectos.")
        return

    resultado = [] #igual que antes, aquí guardaremos los resultados que encontremos en el recorrido del bucle for
    no_encontrado=True
    for pais in lista:

        if minimo <= pais["poblacion"] <= maximo:
            resultado.append(pais)
            no_encontrado=False
    if no_encontrado==True:
        print("no se encontraron coincidencias")
    mostrar(resultado)


def filtrar_superficie(lista):

    try:
        minimo = int(input("Superficie mínima: "))
        if minimo<0:
            print("ingrese un número válido")
            return
        maximo = int(input("Superficie máxima: "))
        if maximo<0:
            print("ingrese un número válido")
    except:
        print("Valores incorrectos.")
        return

    resultado = []

    for pais in lista:

        if minimo <= pais["superficie"] <= maximo:
            resultado.append(pais)

    mostrar(resultado)


# ==========================
# ORDENAR
# ==========================

def ordenar(lista):
    print("elija bajo qué criterio quiere ordenar la lista:\n1) nombre\n2)población\3)superficie")


    opcion = input("Opción: ")

    sentido = input("Ascendente(A) Descendente(D): ").upper()

    reversa = sentido == "D"

    if opcion == "1":
        lista.sort(key=lambda x: x["nombre"], reverse=reversa)

    elif opcion == "2":
        lista.sort(key=lambda x: x["poblacion"], reverse=reversa)

    elif opcion == "3":
        lista.sort(key=lambda x: x["superficie"], reverse=reversa)

    else:
        print("Opción incorrecta.")
        return

    mostrar(lista)


# ==========================
# ESTADÍSTICAS
# ==========================

def estadisticas(lista):

    if len(lista) == 0:
        return

    mayor = max(lista, key=lambda x: x["poblacion"])
    menor = min(lista, key=lambda x: x["poblacion"])

    promedio_poblacion = sum(p["poblacion"] for p in lista) / len(lista)

    promedio_superficie = sum(p["superficie"] for p in lista) / len(lista)

    print()

    print("Mayor población:", mayor["nombre"])

    print("Menor población:", menor["nombre"])

    print("Promedio población:", round(promedio_poblacion, 2))

    print("Promedio superficie:", round(promedio_superficie, 2))

    continentes = {}

    for pais in lista:

        cont = pais["continente"]

        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    print()

    print("Cantidad por continente:")

    for c in continentes:
        print(c, ":", continentes[c])
