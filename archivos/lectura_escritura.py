"""
Python hace que la E/S de archivos sea simple. Echa un vistazo
a cómo leer y escribir archivos aquí:

https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Abre el archivo "foo.txt" (que ya existe) para lectura
# Imprime todo el contenido del archivo y luego cierra el archivo
# Nota: presta atención al directorio actual al intentar abrir "foo.txt"

with open("foo.txt", "r") as foo_file:
    contents = foo_file.read()
    print(contents)

# Abre un archivo llamado "bar.txt" (que aún no existe) para
# escritura. Escribe tres líneas de contenido arbitrario en ese archivo,
# luego cierra el archivo. Abre "bar.txt" e inspéctalo para asegurarte
# de que contiene lo que esperas que contenga.

with open("bar.txt", "w") as bar_file:
    bar_file.write("This is line 1.\n")
    bar_file.write("Here comes line 2.\n")
    bar_file.write("Last but not least, line 3.\n")

# Ahora, abre "bar.txt" para lectura e imprime su contenido para verificar.
with open("bar.txt", "r") as bar_file:
    bar_contents = bar_file.read()
    print(bar_contents)
