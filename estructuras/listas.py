# Para este ejercicio, busca los métodos y funciones disponibles para usar
# con listas en Python.

x = [1, 2, 3]
y = [8, 9, 10]

# Para lo siguiente, NO USES UNA ASIGNACIÓN (=).

# Cambia x para que sea [1, 2, 3, 4]
x.append(4)
print(x)

# Usando y, cambia x para que sea [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print(x)

# Cambia x para que sea [1, 2, 3, 4, 9, 10]
x.remove(8)
print(x)

# Cambia x para que sea [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print(x)

# Imprime la longitud de la lista x
print(len(x))

# Imprime todos los valores en x multiplicados por 1000
print([val * 1000 for val in x])
