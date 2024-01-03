"""
Las tuplas en Python son similares a las listas, excepto que son inmutables y
generalmente se utilizan para contener datos heterogéneos, a diferencia de las listas,
que suelen utilizarse para contener datos homogéneos. Las tuplas usan paréntesis en lugar
de corchetes cuadrados.

Más específicamente, las tuplas son más rápidas que las listas. Si solo quieres definir
un conjunto constante de valores y ese conjunto de valores nunca necesita mutarse, utiliza
una tupla en lugar de una lista.

Además, tu código será más seguro si decides "proteger contra escritura" los datos que
no necesitan cambiar. Las tuplas aplican la inmutabilidad automáticamente.
"""

import math

def dist(a, b):
    """Calcular la distancia entre dos puntos x, y."""
    x0, y0 = a  # Asignación por destructuración
    x1, y1 = b

    return math.sqrt((x1 - x0)**2 + (y1 - y0)**2)

a = (2, 7)   # <-- coordenadas x, y almacenadas en tuplas
b = (-14, 72)

# Imprime "La distancia es: 66.94"
print("La distancia es: {:.2f}".format(dist(a, b)))


# Escribe una función `print_tuple` que imprima todos los valores en una tupla
def print_tuple(tup):
    for value in tup:
        print(value)

t = (1, 2, 5, 7, 99)
print_tuple(t)  # Imprime 1 2 5 7 99, uno por línea

# Declara una tupla de 1 elemento e imprímela
u = (1,)  # Se añadió una coma para hacer que esto funcione
print_tuple(u)
