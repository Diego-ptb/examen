import random
import math
import csv

# Lista de trabajadores
trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

# Diccionario para almacenar los sueldos
sueldos = {}

def asignar_sueldos_aleatorios():
    global sueldos
    sueldos = {trabajador: random.randint(300000, 2500000) for trabajador in trabajadores}
    print("Sueldos aleatorios asignados con éxito.")

def clasificar_sueldos():
    global sueldos
    menor_a_800k = []
    entre_800k_y_2M = []
    mayor_a_2M = []
    total_sueldos = 0
    
    for trabajador, sueldo in sueldos.items():
        total_sueldos += sueldo
        if sueldo < 800000:
            menor_a_800k.append((trabajador, sueldo))
        elif 800000 <= sueldo <= 2000000:
            entre_800k_y_2M.append((trabajador, sueldo))
        else:
            mayor_a_2M.append((trabajador, sueldo))
    
    print("\nSueldos menores a $800.000:")
    for trabajador, sueldo in menor_a_800k:
        print(f"{trabajador}: ${sueldo}")
    print(f"TOTAL: {len(menor_a_800k)}")
    
    print("\nSueldos entre $800.000 y $2.000.000:")
    for trabajador, sueldo in entre_800k_y_2M:
        print(f"{trabajador}: ${sueldo}")
    print(f"TOTAL: {len(entre_800k_y_2M)}")
    
    print("\nSueldos superiores a $2.000.000:")
    for trabajador, sueldo in mayor_a_2M:
        print(f"{trabajador}: ${sueldo}")
    print(f"TOTAL: {len(mayor_a_2M)}")
    
    print(f"\nTOTAL SUELDOS: ${total_sueldos}")

def ver_estadisticas():
    global sueldos
    if not sueldos:
        print("No se han asignado sueldos aún.")
        return
    
    sueldos_lista = list(sueldos.values())
    sueldo_maximo = max(sueldos_lista)
    sueldo_minimo = min(sueldos_lista)
    promedio_sueldos = sum(sueldos_lista) / len(sueldos_lista)
    media_geometrica = math.exp(sum(math.log(sueldo) for sueldo in sueldos_lista) / len(sueldos_lista))
    
    print(f"\nSueldo más alto: ${sueldo_maximo}")
    print(f"Sueldo más bajo: ${sueldo_minimo}")
    print(f"Promedio de sueldos: ${promedio_sueldos:.2f}")
    print(f"Media geométrica de sueldos: ${media_geometrica:.2f}")

def reporte_sueldos():
    global sueldos
    if not sueldos:
        print("No se han asignado sueldos aún.")
        return
    
    archivo_csv = 'reporte_sueldos.csv'
    with open(archivo_csv, mode='w', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])  # Encabezados de las columnas
        
        for trabajador, sueldo in sueldos.items():
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador, f"${sueldo}", f"${descuento_salud:.2f}", f"${descuento_afp:.2f}", f"${sueldo_liquido:.2f}"])
    
    print(f"\nReporte de sueldos exportado a {archivo_csv}")
def fin():
    print("Finalizando programa...\nDesarrollado por Diego Araya\nRUT 20980273-2") 

def mostrar_menu():
    print("\nMenú de Opciones:")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")

def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == '1':
            asignar_sueldos_aleatorios()
        elif opcion == '2':
            clasificar_sueldos()
        elif opcion == '3':
            ver_estadisticas()
        elif opcion == '4':
            reporte_sueldos()
        elif opcion == '5':
            fin()
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 5.")