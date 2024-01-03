# Experimenta con argumentos posicionales, argumentos arbitrarios y argumentos
# de palabras clave.

# Escribe una función f1 que tome dos argumentos posicionales enteros y devuelva
# la suma. Esto es lo que considerarías una función regular y normal.

def f1(x, y):
    return x + y

print(f1(1, 2))

# Escribe una función f2 que tome cualquier cantidad de argumentos enteros y devuelva
# la suma.
# Nota: Busca "python arbitrary arguments" en Google y busca "*args"

def f2(*args):
    return sum(args)

print(f2(1))                    # Debería imprimir 1
print(f2(1, 3))                 # Debería imprimir 4
print(f2(1, 4, -12))            # Debería imprimir -7
print(f2(7, 9, 1, 3, 4, 9, 0))  # Debería imprimir 33

a = [7, 6, 5, 4]

# ¿Cómo debes modificar la llamada a f2 a continuación para que funcione?
print(f2(*a))    # Debería imprimir 22

# Escribe una función f3 que acepte uno o dos argumentos. Si es un argumento,
# devuelve ese valor más 1. Si son dos argumentos, devuelve la suma de los
# argumentos.
# Nota: Busca "python default arguments" para obtener una pista.

def f3(x, y=None):
    return x + (y if y is not None else 1)

print(f3(1, 2))  # Debería imprimir 3
print(f3(8))     # Debería imprimir 9


# Escribe una función f4 que acepte un número arbitrario de argumentos de palabras clave y
# imprima las claves y valores de la siguiente manera:
#
# clave: foo, valor: bar
# clave: baz, valor: 12
#
# Nota: Busca "python keyword arguments".

def f4(**kwargs):
    for key, value in kwargs.items():
        print(f"clave: {key}, valor: {value}")

# Debería imprimir
# clave: a, valor: 12
# clave: b, valor: 30
f4(a=12, b=30)

# Debería imprimir
# clave: ciudad, valor: Zacatecas
# clave: poblacion, valor: 121240
# clave: fundacion, valor: "March 23, 1868"
f4(ciudad="Zacatecas", poblacion=121240, fundacion="17 de Junio de 1546")

d = {
    "superheroe": "spiderman",
    "ID": 1
}

# ¿Cómo debes modificar la llamada a f4 a continuación para que funcione?
f4(**d)
