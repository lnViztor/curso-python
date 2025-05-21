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

###
# 04 - Funciones
# Bloques de código reutilizables y parametrizables para hacer tareas especificas
###

from os import system
if system("clear") != 0: system("cls")

# """ Definición de una función

# def nombre_de_la_funcion(parametro1, parametro2, ...):
#   # docstring
#   # cuerpo de la función
#   return valor_de_retorno # opcional

# """

# # Ejemplo de una función para imprimir algo en consola
# def saludar():
#   print("¡Hola!")

# # Ejemplo de una función con parámetro
# def saludar_a(nombre):
#   print(f"¡Hola {nombre}!")

# saludar_a("midudev")
# saludar_a("madeval")
# saludar_a("pheralb")
# saludar_a("felixicaza")
# saludar_a("Carmen Ansio")

# Funciones con más parámetros
# def sumar(a, b):
#   suma = a + b
#   return suma

# result = sumar(2, 3)
# print(result)

# # Documentar las funciones con docstring
# def restar(a, b):
#   """Resta dos números y devuelve el resultado"""
#   return a - b

# parámetros por defecto
# def multiplicar(a, b = 2):
#   return a * b

# print(multiplicar(2))
# print(multiplicar(2, 3))

# Argumentos por posición
def describir_persona(nombre: str, edad: int, sexo: str):
  print(f"Soy {nombre}, tengo {edad} años y me identifico como {sexo}")

# parámetros son posicionales
describir_persona(1, 25, "gato")
describir_persona("midudev", 25, "gato")
describir_persona("hombre", "madeval", 39)

# Argumentos por clave
# parámetros nombrados
describir_persona(sexo="gato", nombre="midudev", edad=25)
describir_persona(sexo="hombre", nombre="madeval", edad=21) 

# Argumentos de longitud de variable (*args):
def sumar_numeros(*args):
  suma = 0
  for numero in args:
    suma += numero
  return suma

print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2,3 ,4, 5, 6, 7, 8, 9, 10))

# Argumentos de clave-valor variable (**kwargs):
def mostrar_informacion_de(**kwargs):
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")

mostrar_informacion_de(nombre="midudev", edad=25, sexo="gato")
print("\n")
mostrar_informacion_de(name="madeval", edad=21, country="Uruguay")
print("\n")
mostrar_informacion_de(nick="pheralb", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(super_name="felixicaza", es_mod=True, gatos=40)

# Ejercicios
# Volver a los ejercicios anteriores
# y convertirlos en funciones
# e intentar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
# Ejercicio 1: Imprimir números del 1 al 10
def imprimir_numeros_1_a_10():
  lista = []
  for i in range(1, 11):
    #meterlo en una lista
    lista.append(i)
  return lista
print(imprimir_numeros_1_a_10())

# Ejercicio 2: Imprimir números impares del 1 al 20
def imprimir_numeros_impares_1_a_20():
  lista = []
  for i in range(1, 21, 2):
    #meterlo en una lista
    lista.append(i)
  return lista
print(imprimir_numeros_impares_1_a_20())

#Ejercicio 3:
def calcular_total(precio_base, descuento=0, impuesto=0):
  """Calcula el precio total aplicando descuento e impuesto"""
  precio_con_descuento = precio_base - (precio_base * descuento)
  precio_final = precio_con_descuento + (precio_con_descuento * impuesto)
  return round(precio_final)

print(calcular_total(100, 0.1, 0.16)) # precio_base=100, descuento=10%, impuesto=20%