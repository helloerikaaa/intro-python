# Experimenta con los alcances en Python.
# Buena lectura: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# Cuando usas una variable en una función, su ámbito es local a la función.
x = 12

def change_x():
    global x  # Agrega la palabra clave global para referenciar la variable global
    x = 99

change_x()

# Esto imprime 99. ¿Qué tenemos que modificar en change_x() para que imprima 99?
print(x)


# Esta función anidada tiene un problema similar.

def outer():
    y = 120

    def inner():
        nonlocal y  # Agrega la palabra clave nonlocal para referenciar la variable de la función externa
        y = 999

    inner()

    # Esto imprime 999. ¿Qué tenemos que cambiar en inner() para que imprima
    # 999?
    # Nota: Busca "python nested function scope".
    print(y)


outer()
