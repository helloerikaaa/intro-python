"""
Python expone una sintaxis concisa e intuitiva para realizar
rebanado (slicing) en listas y cadenas. Esto facilita hacer
referencia solo a una parte de una lista o cadena.

Usa la sintaxis de rebanado (slice) de Python para lograr lo siguiente:
"""

a = [2, 4, 1, 7, 9, 6]

# Imprime el segundo elemento: 4
print(a[1])

# Imprime el segundo desde el último elemento: 9
print(a[-2])

# Imprime los últimos tres elementos en el array: [7, 9, 6]
print(a[-3:])

# Imprime los dos elementos del medio en el array: [1, 7]
print(a[2:4])

# Imprime todos los elementos excepto el primero: [4, 1, 7, 9, 6]
print(a[1:])

# Imprime todos los elementos excepto el último: [2, 4, 1, 7, 9]
print(a[:-1])

# Para la cadena s...
s = "Hello, world!"

# Imprime solo los caracteres del 8 al 12: "world"
print(s[7:12])
