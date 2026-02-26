from flask import Flask, render_template, request, redirect
import os

app = Flask(__name__)

ARCHIVO = "estudiantes.txt"


# crear archivo si no existe
if not os.path.exists(ARCHIVO):
    open(ARCHIVO, "w", encoding="utf-8").close()


# PAGINA PRINCIPAL
@app.route("/")
def index():
    return render_template("index.html")


# AGREGAR ESTUDIANTE
@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        nota1 = float(request.form["nota1"])
        nota2 = float(request.form["nota2"])
        nota3 = float(request.form["nota3"])

        # validar notas
        if nota1 > 5 or nota2 > 5 or nota3 > 5:
            return "Error: las notas no pueden ser mayores a 5"

        with open(ARCHIVO, "a", encoding="utf-8") as archivo:
            archivo.write(f"{nombre},{nota1},{nota2},{nota3}\n")

        return redirect("/ver")

    return render_template("agregar.html")


# VER ESTUDIANTES
@app.route("/ver")
def ver():
    estudiantes = []

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")

            if len(datos) == 4:
                nombre = datos[0]
                n1 = float(datos[1])
                n2 = float(datos[2])
                n3 = float(datos[3])
                promedio = round((n1 + n2 + n3) / 3, 2)

                estudiantes.append({
                    "nombre": nombre,
                    "nota1": n1,
                    "nota2": n2,
                    "nota3": n3,
                    "promedio": promedio
                })

    return render_template("ver.html", estudiantes=estudiantes)


# MEJOR ESTUDIANTE
@app.route("/mejor")
def mejor():
    mejor_est = None
    mejor_prom = 0

    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
        for linea in archivo:
            datos = linea.strip().split(",")

            if len(datos) == 4:
                nombre = datos[0]
                n1 = float(datos[1])
                n2 = float(datos[2])
                n3 = float(datos[3])
                promedio = (n1 + n2 + n3) / 3

                if promedio > mejor_prom:
                    mejor_prom = promedio
                    mejor_est = {
                        "nombre": nombre,
                        "promedio": round(promedio, 2)
                    }

    return render_template("mejor.html", mejor=mejor_est)


# BUSCAR ESTUDIANTE
@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultado = None

    if request.method == "POST":
        nombre_buscar = request.form["nombre"].lower()

        with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")

                if len(datos) == 4:
                    nombre = datos[0].lower()

                    if nombre_buscar in nombre:
                        n1 = float(datos[1])
                        n2 = float(datos[2])
                        n3 = float(datos[3])
                        promedio = round((n1 + n2 + n3) / 3, 2)

                        resultado = {
                            "nombre": datos[0],
                            "nota1": n1,
                            "nota2": n2,
                            "nota3": n3,
                            "promedio": promedio
                        }

    return render_template("buscar.html", resultado=resultado)


# IMPORTANTE PARA RENDER
if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=puerto)
  



