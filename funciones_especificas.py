from funciones_generales import *

# ----------------------------------------------
# Crea una matriz de tamaño filas x columnas, con un valor inicial en cada celda
# ----------------------------------------------
def crear_matriz(valor, filas, columnas):
    matriz = []
    for i in range(filas):  # Recorre cada fila
        fila = [valor] * columnas  # Crea una fila con el valor repetido 'columnas' veces
        matriz += [fila]  # Agrega la fila a la matriz
    return matriz  # Devuelve la matriz completa


# ----------------------------------------------
# Muestra en pantalla el contenido de la matriz en formato tabular
# ----------------------------------------------
def mostrar_matriz(matriz):
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            print(f"{matriz[i][j]:3}", end=" ")  # Imprime cada valor con formato
        print(" ")  # Salto de línea al terminar una fila


# ----------------------------------------------
# Registra la cantidad de servicios realizados por veterinario
# ----------------------------------------------
def registrar_turnos(matriz_veterinario: list, vector_veterinario: list, vector_precio: list, vector_servicio: list):
    
    continuar = "si"
    while continuar == "si":  # Permite ingresar varios registros

        # Selección del veterinario
        posicion_veterinario = validar_eleccion("Ingrese nombre del veterinario", vector_veterinario, "Lista de Veterinarios")
        
        # Selección del servicio
        posicion_servicio = validar_eleccion("Ingrese un servicio", vector_servicio, "Tipos de Servicios")

        # Cantidad de servicios realizados (entre 1 y 10)
        cantidad_servicios = ingreso_int("Ingrese cantidad de servicios (1 - 10)")

        # Se guarda la cantidad en la posición correspondiente de la matriz
        matriz_veterinario[posicion_veterinario][posicion_servicio] += cantidad_servicios

        # Cálculo del total en pesos (cantidad * precio unitario)
        total_pesos = cantidad_servicios * vector_precio[posicion_servicio]
        print(f"✅ Turno registrado: {vector_veterinario[posicion_veterinario]} - {vector_servicio[posicion_servicio]} - Total en pesos: ${total_pesos}")

        # Pregunta si desea seguir ingresando
        continuar = ingreso_string("¿DESEA SEGUIR INGRESANDO DATOS? (si/no): ").lower()
    
    return matriz_veterinario


# ----------------------------------------------
# Muestra todos los datos cargados (veterinarios, servicios, precios y turnos)
# ----------------------------------------------
def visualizar_datos(matriz_veterinarios: list, vector_veterinarios: list, vector_servicios: list, vector_precios: list):
    
    # Ordena los veterinarios (y la matriz asociada) alfabéticamente
    ordenamiento_datos(matriz_veterinarios, vector_veterinarios)

    print("VETERINARIO            SERVICIO                 PRECIO($)            TURNOS")
    print("------------------------------------------------------------------------------")

    # Recorre veterinarios
    for i in range(len(vector_veterinarios)):
        print(f"{vector_veterinarios[i]}")
        # Recorre servicios
        for j in range(len(vector_servicios)):
            cantidad = matriz_veterinarios[i][j]
            
            if cantidad >= 0:  # Muestra solo valores válidos
                print(f"                {vector_servicios[j]:25}{vector_precios[j]:15} ${cantidad:18}")
        print("------------------------------------------------------------------------------")


# ----------------------------------------------
# Muestra la cantidad total de servicios realizados por cada veterinario
# ----------------------------------------------
def cantidad_servicios_total_por_veterinario(matriz: list, vector_veterinarios: list):  
    print("VETERINARIO           LINEA           TOTAL SERVICOS ")
    print("")
    for i in range(len(matriz)):  # Recorre cada fila (veterinario)
        acumulador = suma_fila(matriz, i)  # Suma todos los valores de esa fila
        print(f"{vector_veterinarios[i]:10}  {i + 1:12}   {acumulador:18}")
        print("--------------------------------------------")


# ----------------------------------------------
# Calcula el promedio de turnos por servicio o muestra el de mayor promedio
# ----------------------------------------------
def promedio_por_servicio(matriz: list, vector_servicios: list, bandera: bool):
    maximo = 0  # Guarda el mayor promedio

    # Recorre columnas (servicios)
    for j in range(len(matriz[0])):
        acumulador = 0
        contador = 0
        # Recorre filas (veterinarios)
        for i in range(len(matriz)):
            acumulador += matriz[i][j]
            contador += 1
        
        promedio_servicio = calculo_promedio(acumulador, contador)
        
        # Si bandera=True, muestra todos los promedios
        if bandera == True:
            print(f"EL PROMEDIO DE TURNOS DEL SERVICIO {vector_servicios[j]} = {promedio_servicio}")
            print(" ")
        else:
            # Si bandera=False, busca el mayor promedio
            if bandera == True or promedio_servicio > maximo:
                maximo = promedio_servicio
                servicio_maximo = vector_servicios[j]
                promedio_maximo = maximo
    
    # Si no se imprimieron todos, muestra solo el máximo
    if bandera == False:
        print(f"EL SERVICIO {servicio_maximo} TIENE EL MAYOR PROMEDIO: {promedio_maximo}")


# ----------------------------------------------
# Calcula la recaudación total de cada veterinario
# y el total general de la veterinaria
# ----------------------------------------------
def recaudo_servicios(matriz: list, vector_nombres: list, vector_precios: list, matriz_totales: list, bandera: bool) -> int:

    total_recaudacion_de_la_veterinaria = 0
    
    # Calcula cuánto recaudó cada veterinario
    for i in range(len(matriz)):
        calculo = 0
        for j in range(len(matriz[i])):
            calculo += matriz[i][j] * vector_precios[j]  # cantidad * precio
            matriz_totales[i][0] = vector_nombres[i]     # Guarda el nombre
            matriz_totales[i][1] = calculo               # Guarda el total recaudado

    # Ordena los veterinarios alfabéticamente junto a sus totales
    for i in range(len(matriz_totales) - 1):
        for j in range(i + 1, len(matriz_totales)):
            if matriz_totales[i][0] > matriz_totales[j][0]:
                auxiliar = matriz_totales[i]
                matriz_totales[i] = matriz_totales[j]
                matriz_totales[j] = auxiliar

    # Si bandera=True, se muestra el detalle
    if bandera == True:
        print("VETERINARIO A/Z                    RECAUDO TOTAL $")
        print("--------------------------------------------------")
        print(" ")

    # Se recorre la matriz ordenada para mostrar o acumular el total
    for i in range(len(matriz_totales)):
        nombre = matriz_totales[i][0]
        total_por_veterinario = matriz_totales[i][1]
        total_recaudacion_de_la_veterinaria += total_por_veterinario
        
        if bandera == True:
            print(f"{nombre:25}               {total_por_veterinario} $")
            print("--------------------------------------------------")
            print(" ")

    # Si bandera=False, devuelve el total general
    if bandera == False:
        return total_recaudacion_de_la_veterinaria


# ----------------------------------------------
# Calcula el porcentaje de turnos que representa cada servicio
# ----------------------------------------------
def porcentaje_servicios(matriz_veterinarios: list, vector_servicios: list):
    
    total_turnos = 0
    turnos_por_servicio = [0] * len(vector_servicios)

    # Suma la cantidad total de turnos y acumula por servicio
    for i in range(len(matriz_veterinarios)):
        for j in range(len(matriz_veterinarios[i])):
            turnos_por_servicio[j] += matriz_veterinarios[i][j]
            total_turnos += matriz_veterinarios[i][j]

    print(" Servicio                    % Por Servicio")
    print(" ")
    
    # Calcula el porcentaje de cada servicio sobre el total
    for j in range(len(vector_servicios)):
        
        if total_turnos > 0:
            porcentaje = calculo_porcentaje(turnos_por_servicio[j], total_turnos)
        else:
            porcentaje = 0
        
        print(f"{vector_servicios[j]:25} {porcentaje} %")
        print(" ")


# ----------------------------------------------
# Muestra el/los veterinarios con menor cantidad de turnos
# ----------------------------------------------
def veterinario_menor_turnos(matriz_veterinarios: list, vector_veterinarios: list):
    
    menor_total = 0
    nombres_turnos_menores = []

    for i in range(len(matriz_veterinarios)):  # Recorre cada veterinario
        total = suma_fila(matriz_veterinarios, i)  # Total de turnos del veterinario
        
        # Si es el primer valor o es menor que el actual menor, se actualiza
        if menor_total == 0 or total < menor_total:
            menor_total = total
            nombres_turnos_menores = [vector_veterinarios[i]]
        # Si empata con el menor, se agrega al listado
        elif total == menor_total:
            nombres_turnos_menores += [vector_veterinarios[i]]

    print(f"Veterinario/s con menor cantidad de turnos: ({menor_total} turnos) es/son: ")
    
    # Muestra todos los nombres con el menor total
    for i in range(len(nombres_turnos_menores)):
        print(f"- {nombres_turnos_menores[i]}")


# ----------------------------------------------
# Calcula el porcentaje de turnos realizados por cada veterinario
# ----------------------------------------------
def porcentaje_turnos_por_veterinario(matriz_veterinarios: list, vector_veterinarios: list):
    
    total_turnos = 0
    porcentaje_total = 0
    total_por_veterinario = [0] * len(vector_veterinarios)

    # Suma los turnos por veterinario
    for i in range(len(matriz_veterinarios)):
        total_por_veterinario[i] = suma_fila(matriz_veterinarios, i)
        total_turnos += total_por_veterinario[i]
    
    print(f"Total de turnos: {total_turnos}")
    print(" ")

    print("PORCENTAJE DE TURNOS POR VETERINARIO:")
    print(" ")
    
    # Calcula el porcentaje que representa cada veterinario sobre el total
    for i in range(len(vector_veterinarios)):
        
        if total_turnos > 0:
            porcentaje = calculo_porcentaje(total_por_veterinario[i], total_turnos)
            porcentaje_total += porcentaje
        else:
            porcentaje = 0
        
        print(f"{vector_veterinarios[i]:25} = {porcentaje} %")
        print(" ")
    
    print(f"El porcentaje total es de    =     {porcentaje_total} %")


# ----------------------------------------------
# Calcula qué veterinarios superan el promedio general de recaudación
# ----------------------------------------------
def listado_mayor_promedio_recaudacion(matriz: list, vector_veterinarios: list, vector_precios: list):
    total_acumulador = 0
    veterinario_recaudacion = 0

    # Calcula el total general de recaudación
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total_acumulador += matriz[i][j] * vector_precios[j]
    
    # Calcula el promedio general
    total_promedio_recaudacion = calculo_promedio(total_acumulador, len(matriz))

    print(f"el promedio total: {total_promedio_recaudacion}")
    print("____________________________________________________")
    print(" ")
    print("Lista de Veterinarios con mayor porcentaje que el total")
    print("_________________________________________________________________")
    print(" ")

    # Recorre cada veterinario y calcula su recaudación
    for i in range(len(matriz)):
        veterinario_recaudacion = 0
        for j in range(len(matriz[i])):
            veterinario_recaudacion += matriz[i][j] * vector_precios[j]
        
        # Promedio individual
        promedio_por_veterinario_recaudacion = veterinario_recaudacion / len(vector_precios)
        
        # Si supera el promedio general, se muestra
        if promedio_por_veterinario_recaudacion > total_promedio_recaudacion:
            print(f"El Veterinario {vector_veterinarios[i]} Tiene un promedio de {promedio_por_veterinario_recaudacion}")
            print("___________")


# ----------------------------------------------
# Muestra para cada veterinario cuál fue su servicio más solicitado
# ----------------------------------------------
def servicio_mas_solicitado_por_veterinario(matriz_veterinario: list, vector_servicio: list, vector_veterinario: list):
    print("VETERINARIO     SERVICIO MAS SOLICITADO         CANTIDAD")
    print("________________________________________________________")
    print(" ")
    
    for i in range(len(matriz_veterinario)):  # Recorre cada veterinario
        servicio_mas_solicitado = ""
        bandera_maximo = False
        maximo = 0    

        # Busca el servicio más solicitado del veterinario actual
        for j in range(len(matriz_veterinario[i])):
            acumulador_servicio = matriz_veterinario[i][j]
            
            if not bandera_maximo or acumulador_servicio > maximo:
                maximo = acumulador_servicio
                servicio_mas_solicitado = vector_servicio[j]
                bandera_maximo = True
        
        # Muestra el resultado del veterinario actual
        print(f"{vector_veterinario[i]:20}{servicio_mas_solicitado:20}{maximo:10}")                   
        print(" ")
        print("--------------------------------------------------------")
        print(" ")

#########################################################

def menos_variacion_servicios(matriz, vector_servicios):

    bandera_menor = False
    lista_variacion = [0] * len(vector_servicios)
    menor = 0

    for j in range(len(matriz[0])):
        acumulador = 0
        acumulador_total = 0
        total = 0
        bandera = False
        for i in range(len(matriz)):
            
            if bandera == False:
                acumulador = matriz[i][j]
                bandera = True
            
            elif bandera == True:
                acumulador_total = acumulador - matriz[i][j]
                if acumulador_total < 0:
                    acumulador_total *= - 1
                
                total += acumulador_total
                bandera = False

        lista_variacion[j] = total

    
    for i in range(len(lista_variacion)):
        print(f"servicio: {vector_servicios[i]} cantidad: {lista_variacion[i]}")
        print("")
        
        if bandera_menor == False or lista_variacion[i] < menor:
            menor = lista_variacion[i]
            servicio_menor = vector_servicios[i]
            bandera_menor = True
    
    print("______________________________")
    print("")
    print(f"servicio con menos variacion: {servicio_menor} cantidad: {menor}")