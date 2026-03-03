from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

archivo = "estudiantes.txt"


if not os.path.exists(archivo):
    open(archivo, "w").close()





def cargar_estudiantes():
    estudiantes = []

    with open(archivo, "r") as f:
        for linea in f:
            datos = linea.strip().split(",")

            if len(datos) == 5:
                estudiantes.append({
                    "nombre": datos[0],
                    "nota1": float(datos[1]),
                    "nota2": float(datos[2]),
                    "nota3": float(datos[3]),
                    "promedio": float(datos[4])
                })

    return estudiantes





def guardar_estudiante(nombre, n1, n2, n3, promedio):

    with open(archivo, "a") as f:
        f.write(f"{nombre},{n1},{n2},{n3},{promedio}\n")





@app.route("/")
def inicio():

    return render_template("index.html")





@app.route("/agregar", methods=["GET", "POST"])
def agregar():

    if request.method == "POST":

        nombre = request.form["nombre"]

        n1 = float(request.form["nota1"])
        n2 = float(request.form["nota2"])
        n3 = float(request.form["nota3"])

        if not (1 <= n1 <= 5 and 1 <= n2 <= 5 and 1 <= n3 <= 5):
            return "Error: las notas deben estar entre 1 y 5"

        promedio = round((n1 + n2 + n3) / 3, 2)

        guardar_estudiante(nombre, n1, n2, n3, promedio)

        return redirect("/ver")

    return render_template("agregar.html")





@app.route("/ver")
def ver():

    estudiantes = cargar_estudiantes()

    return render_template("ver.html", estudiantes=estudiantes)



@app.route("/mejor")
def mejor():

    estudiantes = cargar_estudiantes()

    if not estudiantes:
        return "No hay estudiantes"

    mejor_est = max(estudiantes, key=lambda x: x["promedio"])

    return render_template("mejor.html", mejor=mejor_est)



@app.route("/buscar", methods=["GET", "POST"])
def buscar():
    resultado = None
    
    if request.method == "POST":
        nombre_buscar = request.form["nombre"].lower()
        
        with open("estudiantes.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split(",")
                nombre = datos[0].lower()
                
                if nombre_buscar in nombre:
                    resultado = datos
    
    return render_template("buscar.html", resultado=resultado)



if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=puerto)
  





