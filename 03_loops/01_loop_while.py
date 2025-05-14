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

###
# 01 - Bucles (while)
# Permiten ejecutar un bloque de código repetidamente mientras se cumpla una condición
###

from os import system
if system("clear") != 0: system("cls")

print("\n Bucle while:")

# Bucle con una simple condición
contador = 0

while contador <= 5:
  print(contador)
  contador += 1 # es super importante para evitar un bucle infinito

# utilizando la palabra break, para romper el bucle
print("\n Bucle while con break:")
contador = 0

while True:
  print(contador)
  contador += 1
  if contador == 5:
    break # sale del bucle

# continue, que lo hace es saltar esa iteración en concreto
# y continuar con el bucle
print("\n Bucle con continue")
contador = 0
while contador < 10:
  contador += 1

  if contador % 2 == 0:
    continue

  print(contador)

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# else, esta condición cuando se ejecuta?
print("\n Bucle while con else:")
contador = 0
while contador < 5:
  print(contador)
  contador += 1
else:
  print("El bucle ha terminado")

# pedirle al usuario un número que tiene
# que ser positivo si no, no le dejamos en paz
numero = -1
while numero < 0:
  numero = int(input("Escribe un número positivo: "))
  if numero < 0:
    print("El número debe ser positivo. Intenta otra vez, majo o maja.")

print(f"El número que has introducido es {numero}")

numero = -1
while numero < 0:
  try:
    numero = int(input("Escribe un número positivo: "))
    if numero < 0:
      print("El número debe ser positivo. Intenta otra vez, majo o maja.")
  except ValueError:
    print("Lo que introduces debe ser un número, que si no peta!")

print(f"El número que has introducido es {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
# Luego imprime "¡Despegue!".
contador = 10
while contador > 0:
    print(contador)
    contador -= 1
print("¡Despegue!")# Ejercicio 1: Cuenta atrás
print("\nEjercicio 1:")


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")
# Inicializa la variable de suma
suma = 0
# Inicializa el contador
contador = 1
# El usuario introduce el numero
numero = int(input("Escribe un número positivo: "))
# Bucle while para recorrer los números del 1 al 20
while contador <= numero:
    # Verifica si el número es par
    if contador % 2 == 0:
        #Muestra el número par
        print(f"El número par es: {contador}")
        # Suma el número par a la variable de suma
        suma += contador
    # Incrementa el contador
    contador += 1
# Imprime la suma total
print(f"La suma de los números pares entre 1 y {numero} es: {suma}")



# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")
# Inicializa la variable de factorial
factorial = 1
# Inicializa el contador
contador = 1
# El usuario introduce el numero
numero = int(input("Escribe un número positivo: "))
# Bucle while para calcular el factorial
while contador <= numero:
    # Verifica si el número es positivo
    if numero < 0:
        print("El número debe ser positivo. Intenta otra vez, majo o maja.")
        break
    #Pinta la operación
    print(f"{factorial} * {contador} = {factorial * contador}")
    # Multiplica el factorial por el contador
    factorial *= contador
    # Incrementa el contador
    contador += 1
# Imprime el resultado
print(f"El factorial de {numero} es: {factorial}")


# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")
# Inicializa la variable de contraseña
contraseña = ""
# Bucle while para validar la contraseña
while len(contraseña) < 8:
    # Pide al usuario que introduzca una contraseña
    contraseña = input("Introduce una contraseña (mínimo 8 caracteres): ")
    # Verifica si la contraseña es válida
    if len(contraseña) < 8:
        print("La contraseña debe tener al menos 8 caracteres. Intenta otra vez.")
    else:
        print("Contraseña válida")
        

# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")
# Inicializa el contador
contador = 1
# El usuario introduce el numero
numero = int(input("Escribe un número para ver su tabla de multiplicar: "))
# Bucle while para imprimir la tabla de multiplicar
while contador <= 10:
    # Imprime la multiplicación
    print(f"{numero} x {contador} = {numero * contador}")
    # Incrementa el contador
    contador += 1

# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.
#Definición de número primo: Un número primo es un número natural mayor que 1 que 
# no tiene divisores positivos más que 1 y sí mismo.
print("\nEjercicio 6:")
# Inicializa el contador
contador = 2
# El usuario introduce el numero
numero = int(input("Escribe un número positivo: "))
# Bucle while para imprimir los números primos  
while contador <= numero:
    # Inicializa la variable de primo
    primo = True
    # Bucle para verificar si el número es primo
    divisor = 2
    while divisor < contador:
        if contador % divisor == 0:
            primo = False
            break
        divisor += 1
    # Imprime el número primo
    if primo:
        print(contador)
    # Incrementa el contador
    contador += 1
