import csv





#GUARDAR DATOS

def guardar_cambios(lista):
    with open("CSV/dominio.csv", "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")

        for pais in lista:
            archivo.write(
                f"{pais['Nombre']},"
                f"{pais['Poblacion']},"
                f"{pais['Superficie']},"
                f"{pais['Continente']}\n"
            )


# ==========================
# MOSTRAR
# ==========================

def mostrar(lista): #con esta función mostramos la lista de países acorde a los parámetros que le demos en el momento que llamamos la función

    if len(lista) == 0:
        print("No hay datos.")
        return

    for pais in lista:
        print("-----------------------------")
        print("Nombre:", pais["Nombre"])
        print("Población:", pais["Poblacion"])
        print("Superficie:", pais["Superficie"])
        print("Continente:", pais["Continente"])


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
        if pais["Nombre"].lower() == nombre.lower():
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
        "Nombre": nombre,
        "Poblacion": poblacion,
        "Superficie": superficie,
        "Continente": continente
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

        if pais["Nombre"].lower() == nombre.lower(): #cuando encuentre una coincidencia en la lista, entramos al IF
            no_encontrado=False
            try:
                pais["Poblacion"] = int(input("ingrese la nueva población: "))
                if pais["Poblacion"]==0:
                    raise ValueError("la nueva población no puede ser cero")
                pais["Superficie"] = int(input("ingrese su nueva superficie: "))
                if pais["Superficie"]==0:
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

        if texto in pais["Nombre"].lower():
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
        if pais["Continente"].lower() == continente:
            resultado.append(pais)
            no_encontrado=False
    if no_encontrado==True:
        print("no se encontraron resultados para el continente escrito: ", continente)
        return
    mostrar(resultado)


def filtrar_poblacion(lista):#sus funciones son parecidas, casi iguales, a filtrar_continente

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

        if minimo <= pais["Poblacion"] <= maximo:
            resultado.append(pais)
            no_encontrado=False
    if no_encontrado==True:
        print("no se encontraron coincidencias")
    mostrar(resultado)


def filtrar_superficie(lista):#sus funciones son parecidas, casi iguales, a filtrar_continente

    try:
        minimo = int(input("Superficie mínima: "))
        if minimo<=0:
            print("ingrese un número válido")
            return
        maximo = int(input("Superficie máxima: "))
        if maximo<=0:
            print("ingrese un número válido")
    except:
        print("Valores incorrectos.")
        return

    resultado = []

    for pais in lista:

        if minimo <= pais["Superficie"] <= maximo:
            resultado.append(pais)

    mostrar(resultado)


# ==========================
# ORDENAR
# ==========================

def ordenar(lista):
    print("elija bajo qué criterio quiere ordenar la lista:\n1) nombre\n2)población\n3)superficie")


    opcion = input("Opción: ")

    sentido = input("Ascendente(A) Descendente(D): ").upper()
    if sentido not in ["A", "D"]:
        print("Opción incorrecta")
        return

    descendiente=False
    if sentido=="D":
        descendiente=True


    if opcion == "1":
        lista.sort(key=lambda x: x["Nombre"], reverse=descendiente)

    elif opcion == "2":
        lista.sort(key=lambda x: x["Poblacion"], reverse=descendiente)

    elif opcion == "3":
        lista.sort(key=lambda x: x["Superficie"], reverse=descendiente)

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

    mayor = max(lista, key=lambda x: x["Poblacion"])
    menor = min(lista, key=lambda x: x["Poblacion"])

    promedio_poblacion = sum(p["Poblacion"] for p in lista) / len(lista)

    promedio_superficie = sum(p["Superficie"] for p in lista) / len(lista)

    

    print("Pais con mayor población:", mayor["Nombre"], "-", mayor["Poblacion"])

    print("Pais con menor población:", menor["Nombre"], "-", menor["Poblacion"])

    print("Promedio población:", round(promedio_poblacion, 2))

    print("Promedio Superficie:", round(promedio_superficie, 2))

    continentes = {}

    for pais in lista:

        cont = pais["Continente"]

        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    

    print("Cantidad de paises por continente:")

    for c in continentes:
        print(c, ":", continentes[c])
