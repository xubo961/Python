import json

with open('receta.json', 'r') as fichero:
    datos = json.load(fichero)

print(datos["tiempoPreparacion"])

for ingrediente in datos["ingredientes"]:
    print(ingrediente)
    if ingrediente["nombreIngrediente"] == "Harina":
        print("Habrá bechamel")

print(datos)