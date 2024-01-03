"""
En este ejercicio, estarás explorando el módulo sys,
que te permite acceder a muchas variables y métodos específicos del sistema,
y el módulo os, que te proporciona acceso a funcionalidades del sistema
operativo a un nivel más bajo.
"""

import sys
# Ver la documentación del módulo sys: https://docs.python.org/3.7/library/sys.html

# Imprimir los argumentos de la línea de comandos en sys.argv, uno por línea:
for arg in sys.argv:
    print(arg)

# Imprimir la plataforma del sistema operativo que estás utilizando:
print(sys.platform)

# Imprimir la versión de Python que estás utilizando:
print(sys.version)


import os
# Ver la documentación del módulo OS: https://docs.python.org/3.7/library/os.html

# Imprimir el ID del proceso actual
print(os.getpid())

# Imprimir el directorio de trabajo actual (cwd):
print(os.getcwd())

# Imprimir el nombre de inicio de sesión de tu máquina
print(os.getlogin())
