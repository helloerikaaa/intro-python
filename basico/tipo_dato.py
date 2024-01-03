"""
Python es un lenguaje fuertemente tipado en su núcleo, lo que significa
que los tipos de valores son importantes, especialmente cuando intentamos
realizar operaciones con ellos.

Ten en cuenta que si intentas ejecutar el siguiente código sin realizar ningún
cambio, obtendrás un TypeError diciendo que no puedes realizar una operación
con una cadena y un entero.
"""

x = 5
y = "7"

# Escribe una declaración de impresión que combine x + y en el valor entero 12
print(x + int(y))

# Escribe una declaración de impresión que combine x + y en el valor de cadena 57
print(str(x) + y)
