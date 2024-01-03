"""
Las comprensiones de listas son una característica genial y única de Python.
Básicamente, actúan como una forma concisa y clara de inicializar y poblar
una lista dada alguna expresión que especifica cómo se debe poblar la lista.

Echa un vistazo a https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
para obtener más información sobre las comprensiones de listas.
"""

# Escribe una comprensión de lista para producir el array [1, 2, 3, 4, 5]
y = [i for i in range(1, 6)]
print(y)

# Escribe una comprensión de lista para producir los cubos de los números 0-9:
# [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
y = [i**3 for i in range(10)]
print(y)

# Escribe una comprensión de lista para producir la versión en mayúsculas de todos los
# elementos en el array a. Pista: "foo".upper() es "FOO".
a = ["foo", "bar", "baz"]
y = [word.upper() for word in a]
print(y)

# Usa una comprensión de lista para crear una lista que contenga solo los elementos
# _pares_ que el usuario ingresó en la lista x.
x = input("Ingrese números separados por comas: ").split(',')
y = [int(num) for num in x if int(num) % 2 == 0]
print(y)
