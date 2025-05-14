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