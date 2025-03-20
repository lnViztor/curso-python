if system("clear") != 0: system("cls")

print("\nEjercicio 2:")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))
operacion = input("Introduce la operación (+, -, *, /): ")

if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 == 0:
        print("Error: No se puede dividir por cero.")
    else:
        resultado = num1 / num2
else:
    print("Operación no válida.")

if 'resultado' in locals(): #Comprueba si la variable resultado existe.
    print(f"El resultado es: {resultado}")