"""
Python proporciona varias formas de realizar impresiones. Investiga
cómo imprimir usando el operador printf, el método de cadena `format`
y mediante f-strings.
"""

x = 10
y = 2.24552
z = "Hola!"

# Usando el operador printf (%), imprime lo siguiente insertando los valores de x,
# y, y z:
print("x is %d, y is %.2f, z is \"%s\"" % (x, y, z))

# Usa el método de cadena 'format' para imprimir lo mismo
print("x is {}, y is {:.2f}, z is \"{}\"".format(x, y, z))

# Finalmente, imprime lo mismo usando una f-string
print(f"x is {x}, y is {y:.2f}, z is \"{z}\"")
