from funciones_especificas import *
from funciones_generales import *

vector_veterinarios = ["maximiliano", "octavio", "marina", "christian", "giovanni", "david", "gonzalo", "catriel", "mariano", "felipe"]
vector_servicios = ["CONSULTA GENERAL", "VACUNACION", "CONTROL POST-QUIRÚRGICO"]
vector_precios = [15000,20000,30000]
vector_ganancia = [0,0,0]

# matriz_veterinarios = crear_matriz(0, 10, 3)
matriz_totales = crear_matriz(0,len(vector_veterinarios),2)


matriz_veterinarios = [
    [10, 9, 2],
    [2, 1, 10],
    [7, 6, 5],
    [3, 0, 7],
    [1, 0, 7],
    [8, 3, 1],
    [4, 5, 9],
    [2, 4, 6],
    [9, 2, 3],
    [3, 7, 8] 
]

menos_variacion_servicios(matriz_veterinarios,vector_servicios)

bandera_fin = True
validacion = True

while bandera_fin == True:
    print("\n=====  MENÚ PRINCIPAL  =====")
    print("1. Registrar un turno\n2. Visualizar todos los datos\n3. Consultas\n4. Salir")
    opcion = input("Seleccione una opción: ")

    match opcion:
        case "1":
            print("\n--- REGISTRAR UN TURNO ---")
            print(" ")
            registrar_turnos(matriz_veterinarios, vector_veterinarios, vector_precios, vector_servicios)
        case "2":
            print("\n--- VISUALIZAR TODOS LOS DATOS ---")
            print(" ")
            visualizar_datos(matriz_veterinarios, vector_veterinarios, vector_servicios, vector_precios)
            # mostrar_matriz(matriz_veterinarios)
        case "3":       
            print("\n===== 📊 SUBMENÚ DE CONSULTAS 📊 =====")
            print("1. 📋 Listado con la cantidad total de turnos reservados por cada veterinario.\n2. 📊 Promedio de turnos por tipo de servicio entre todos los veterinarios.\n3. 📈Veterinarios ordenados alfabéticamente de la A-Z junto al total que recaudó enconcepto de servicios\n4. 💲 Recaudación total acumulada por todos los veterinarios.\n5. 📈 Porcentaje de cada tipo de servicio respecto al total general de turnos.\n6. 📉 Veterinario con menor cantidad total de turnos atendidos.\n7. 📉 Porcentaje de turnos por veterinario respecto al total general.\n8. 🏆 Servicio/s más solicitado/s por cada veterinario.\n9. Servicio con mayor promedio\n10. Veterinario con mayor promedio respecto al total\n11. Servicio con menos variacion")
            opcion_sub = input("Seleccione una opción del submenú: ")
            print("__________________________________________________")
            print(" ")

            match opcion_sub:
                case "1":
                    cantidad_servicios_total_por_veterinario(matriz_veterinarios, vector_veterinarios)
                case "2":
                    promedio_por_servicio(matriz_veterinarios, vector_servicios,True)
                case "3":
                    recaudo_servicios(matriz_veterinarios, vector_veterinarios, vector_precios, matriz_totales, True)
                case "4":
                    total = recaudo_servicios(matriz_veterinarios, vector_veterinarios, vector_precios, matriz_totales, False)
                    print(f"La recaudación TOTAL por todos los veterinarios es de: {total} $")
                case "5":
                    porcentaje_servicios(matriz_veterinarios, vector_servicios)
                case "6":
                    veterinario_menor_turnos(matriz_veterinarios, vector_veterinarios)
                case "7":
                    porcentaje_turnos_por_veterinario(matriz_veterinarios, vector_veterinarios)
                case "8":
                    servicio_mas_solicitado_por_veterinario(matriz_veterinarios, vector_servicios, vector_veterinarios)
                case "9":
                    ####     PARTE 3 DE PARCIAL, PUNTO 1     ####
                    promedio_por_servicio(matriz_veterinarios,vector_servicios,False)
                case "10":
                    ####    PARTE 3 DE PARCIAL, PUNTO 2     ####
                    listado_mayor_promedio_recaudacion(matriz_veterinarios,vector_veterinarios,vector_precios)
                case "11":
                    menos_variacion_servicios(matriz_veterinarios,vector_servicios)
                case _:
                    print("⚠️ Opción no válida en el submenú.")
        case "4":
            print("...SALIENDO DEL PROGRAMA...")
            bandera_fin = False
        case _:
            print("⚠️ Opción inválida, por favor elija una opción del menú.")
