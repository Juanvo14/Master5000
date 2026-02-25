import os

archivo = "estudiantes.txt"

# CARGAR ESTUDIANTES DESDE ARCHIVO

def cargar_estudiantes():
    estudiantes = []
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            for linea in f:
                datos = linea.strip().split(",")
                if len(datos) == 5:
                    nombre = datos[0]
                    notas = list(map(float, datos[1:4]))
                    promedio = float(datos[4])

                    estudiantes.append({
                        "nombre": nombre,
                        "notas": notas,
                        "promedio": promedio
                    })
    return estudiantes


# GUARDAR ESTUDIANTES EN ARCHIVO

def guardar_estudiantes(estudiantes):
    with open(archivo, "w") as f:
        for est in estudiantes:
            linea = f"{est['nombre']},{est['notas'][0]},{est['notas'][1]},{est['notas'][2]},{est['promedio']}\n"
            f.write(linea)

# AGREGAR ESTUDIANTE

def agregar_estudiante(estudiantes):
    nombre = input("Nombre del estudiante: ")
    notas = []

    for i in range(1, 4):
        while True:
            entrada = input(f"Ingrese nota {i} (1 a 5): ")

            try:
                nota = float(entrada.replace(",", "."))

                if 0 <= nota <= 5:
                    notas.append(nota)
                    break
                else:
                    print("Error: La nota debe estar entre 1 y 5.")

            except:
                print("Error: Ingrese un número válido.")

    promedio = round(sum(notas) / 3, 2)

    estudiantes.append({
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio
    })

    guardar_estudiantes(estudiantes)
    print("Estudiante agregado correctamente\n")



# VER ESTUDIANTES

def ver_estudiantes(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    for est in estudiantes:
        estado = "Aprueba" if est["promedio"] >= 3.0 else "Reprueba"

        print("\n----------------------------")
        print(f"Nombre: {est['nombre']}")
        print(f"Notas: {est['notas']}")
        print(f"Promedio: {est['promedio']}")
        print(f"Estado: {estado}")
    print()


# MEJOR ESTUDIANTE

def mejor_estudiante(estudiantes):
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    mejor = max(estudiantes, key=lambda x: x["promedio"])

    print("\n🏆 Mejor estudiante:")
    print(f"Nombre: {mejor['nombre']}")
    print(f"Promedio: {mejor['promedio']}\n")



# MENÚ PRINCIPAL

def main():
    estudiantes = cargar_estudiantes()

    while True:
        print("===== MASTER5000 =====")
        print("1. Agregar estudiante")
        print("2. Ver estudiantes")
        print("3. Mejor estudiante")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_estudiante(estudiantes)
        elif opcion == "2":
            ver_estudiantes(estudiantes)
        elif opcion == "3":
            mejor_estudiante(estudiantes)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida\n")

# EJECUCIÓN
if __name__ == "__main__":
    main()
    input("Presione Enter para cerrar...")
