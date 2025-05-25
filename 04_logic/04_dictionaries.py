# pylint: disable=W0311
# pylint: disable=W0120
# pylint: disable=W0120
# pylint: disable=C0103
# pylint: disable=C0321
# pylint: disable=C0301
# pylint: disable=C0114
# pylint: disable=C0304
# pylint: disable=C0303
# pylint: disable=C2401
# pylint: disable=C0116
# pylint: disable=W0621


###
# 04 - Dictionaries
# Los diccionarios son colecciones de pares clave-valor.
# Sirven para almacenar datos relacionados.
###

from os import system
if system("clear") != 0: system("cls")

# ejemplo tipico de diccionario
persona = {
  "nombre": "midudev",
  "edad": 25,
  "es_estudiante": True,
  "calificaciones": [7, 8, 9],
  "socials": {
    "twitter": "@midudev",
    "instagram": "@midudev",
    "facebook": "midudev"
  }
}

# para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# cambiar valores al acceder
persona["nombre"] = "madeval"
persona["calificaciones"][2] = 10

# eliminar completamente una propiedad
del persona["edad"]
# print(persona)

es_estudiante = persona.pop("es_estudiante") 
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = { "name": "miduev", "age": 25 }
b = { "name": "madeval", "es_estudiante": True }

a.update(b)
print(a)

# comprobar si existe una propiedad
print("name" in persona) # False
print("nombre" in persona) # True

# obtener todas las claves
print("\nkeys:")
print(persona.keys())

# obtener todas los valores
print("\nvalues:")
print(persona.values())

# obtener tanto clave como valor
print("\nitems:")
print(persona.items())

for key, value in persona.items():
  print(f"{key}: {value}")