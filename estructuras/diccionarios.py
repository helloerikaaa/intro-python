"""
Los diccionarios son la implementación de Python de arrays asociativos.
No hay mucha diferencia con la versión de Python en comparación con lo que
encontrarías en otros lenguajes (aunque también puedes inicializar y
poblar diccionarios usando comprensiones de la misma manera que haces con
listas).

La documentación se puede encontrar aquí:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Para este ejercicio, tienes una lista de diccionarios. Cada diccionario
tiene las siguientes claves:
    - lat: un entero firmado que representa un valor de latitud
    - lon: un entero firmado que representa un valor de longitud
    - nombre: una cadena de nombre para esta ubicación
"""

lugares = [
    {
        "lat": 43,
        "lon": -121,
        "nombre": "lugar 1"
    },
    {
        "lat": 41,
        "lon": -123,
        "nombre": "lugar 2"
    },
    {
        "lat": 43,
        "lon": -122,
        "nombre": "lugar 3"
    }
]

# Agrega un nuevo punto de referencia a la lista
nuevo_lugar = {
    "lat": 45,
    "lon": -124,
    "nombre": "lugar 4"
}
lugares.append(nuevo_lugar)

# Modifica el diccionario con nombre "a place" para que su valor de longitud
# sea -130 y cambia su nombre a "lugar inválido"
# Nota: Está bien acceder al diccionario usando notación de corchetes en la
# lista de lugares.
lugares[0]["lon"] = -130
lugares[0]["nombre"] = "Lugar inválido"

# Escribe un bucle que imprima todos los valores de campo para todos los lugares
for lugar in lugares:
    print("lat:", lugar["lat"], "lon:", lugar["lon"], "nombre:", lugar["nombre"])
