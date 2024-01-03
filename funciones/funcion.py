# Escribe una función is_even que devuelva True si el número pasado es par.
def is_even(number):
    return number % 2 == 0

# Lee un número desde el teclado
num = input("Ingrese un número: ")
num = int(num)

# Imprime "Par!" si el número es par. De lo contrario, imprime "Impar"
if is_even(num):
    print("Par!")
else:
    print("Impar")
