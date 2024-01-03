# Define una clase LatLon que pueda recibir los parámetros `lat` y `lon` en el constructor
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Define una clase Lugar que pueda recibir los parámetros `nombre`, `lat` y `lon` en el constructor.
# Debería heredar de LatLon utilizando el método `super`.
class Lugar(LatLon):
    def __init__(self, nombre, lat, lon):
        super().__init__(lat, lon)
        self.nombre = nombre

    def __str__(self):
        return f"Lugar({self.nombre}, {self.lat}, {self.lon})"

# Define una clase Geocache que pueda recibir los parámetros `nombre`, `dificultad`,
# `tam`, `lat` y `lon` en el constructor. Debería heredar de Lugar.
class Geocache(Lugar):
    def __init__(self, nombre, dificultad, tam, lat, lon):
        super().__init__(nombre, lat, lon)
        self.dificultad = dificultad
        self.tam = tam

    def __str__(self):
        return f"Geocache({self.nombre}, diff {self.dificultad}, tam {self.tam}, {self.lat}, {self.lon})"

# Crea un nuevo Lugar e imprímelo: "Bufa", 41.70505, -121.51521
Lugar = Lugar("Bufa", 41.70505, -121.51521)

# Sin cambiar la siguiente línea, ¿cómo puedes hacer que imprima algo
# más legible para los humanos? Pista: Busca el método `object.__str__`.
print(Lugar)

# Crea una nueva geocache "Centro Histórico", diff 1.5, tam 2, 44.052137, -121.41556
geocache = Geocache("Centro Histórico", 1.5, 2, 44.052137, -121.41556)

# Imprímelo, también haz que la impresión sea más legible
print(geocache)
