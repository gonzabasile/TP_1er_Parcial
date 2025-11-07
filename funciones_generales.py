###  INGRESO  ###

def ingreso_string(mensaje: str):
    ingreso = input(f"{mensaje}: ")

    return ingreso


def ingreso_int(mensaje: str):

    bandera_numero = False

    while bandera_numero == False: 
        ingreso_numero = input(f"{mensaje}: ")
        transformacion_numero = int(ingreso_numero)
        
        if transformacion_numero >= 1 and transformacion_numero <= 10:
            bandera_numero = True
            break
        else:
            mensaje = "ERROR... reeingrese cantidad de servicios (1 - 10)"

    return transformacion_numero

################################

### VALIDACION DE ELECCION DE NOMBRE O TIPO DE SERVICIO


def validar_eleccion(mensaje, lista, tipo_lista) -> int:
    bandera = False

    print(f"{tipo_lista}")
    print("_________________")
    mostrar_datos_lista(lista)
    print("_______________________")
    print("")

    while bandera == False:
        eleccion = ingreso_string(mensaje).lower()
        for i in range(len(lista)):
            
            if eleccion == lista[i].lower():
                numero_posicion = i
                bandera = True
                break
        
        if bandera != True:
            print("ERROR... dato no encontrado, reingrese.")

    return numero_posicion


# PRINTEO DE LAS LISTAS (NOMBRES O TIPO DE SERVICIOS)

def mostrar_datos_lista(lista_elementos: list):
    print("")
    
    for i in range(len(lista_elementos)):
            print(f" {i + 1} - {lista_elementos[i]}")
            print("-----")

############################

###   ORDENAMIENTO  ###


def ordenamiento_datos(matriz_veterinarios,vector_veterinarios):
    
    # ordenamos veterinarios de la A-Z
    for i in range(len(vector_veterinarios) - 1):
        for j in range(i + 1, len(vector_veterinarios)):
            if vector_veterinarios[i] > vector_veterinarios[j]:
                
                aux_nombre = vector_veterinarios[i]
                vector_veterinarios[i] = vector_veterinarios[j]
                vector_veterinarios[j] = aux_nombre

                # Intercambiamos también la fila correspondiente en la matriz
                aux_fila = matriz_veterinarios[i]
                matriz_veterinarios[i] = matriz_veterinarios[j]
                matriz_veterinarios[j] = aux_fila

######################


### CALCULO PROMEDIO

def calculo_promedio(numero_1: int, numero_2: int):
    
    calculo = numero_1 / numero_2

    return calculo

######################


### CALCULO PORCENTAJE

def calculo_porcentaje(numero_1: int, numero_2: int):
    
    calculo = (numero_1 * 100) / numero_2

    return calculo

#######################

def suma_fila(matriz: list, fila: list) -> int:
        
        acumulador = 0

        for j in range(len(matriz[fila])):
            acumulador += matriz[fila][j]
        
        return acumulador



