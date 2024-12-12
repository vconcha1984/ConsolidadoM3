# Lista de nombres
nombres = ["Harry Houdini", "Newton", "David Blaine", "Hawking", "Messi", "Teller", "Einstein", "Pele", "Juanes"]

# Listas para magos, científicos y otros
magos = ["Harry Houdini", "David Blaine", "Teller"]
cientificos = ["Newton", "Hawking", "Einstein"]
otros = [nombre for nombre in nombres if nombre not in magos and nombre not in cientificos]

# Función para hacer grandiosos a los magos
def hacer_grandioso(lista_magos):
    for i in range(len(lista_magos)):
        lista_magos[i] = "El gran " + lista_magos[i]

# Función para imprimir nombres
def imprimir_nombres(lista):
    for nombre in lista:
        print(nombre)

# Imprimir lista completa antes de modificar
print("Lista completa de nombres antes de modificar:")
imprimir_nombres(nombres)
print("\n")

# Hacer grandiosos a los magos
hacer_grandioso(magos)

# Imprimir listas después de modificar
print("Nombres de los magos grandiosos:")
imprimir_nombres(magos)
print("\n")

print("Nombres de los científicos:")
imprimir_nombres(cientificos)
print("\n")

print("Nombres de los otros:")
imprimir_nombres(otros)
