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
# pylint: disable=C0413
# pylint: disable=W0105
# pylint: disable=C0325
import re

# [:] Coincide con cualquier caracter dentro de los corchetes

username = "rub.ius_69+"
pattern = r"^[\w._%+-]+$"

match = re.search(pattern, username)
if match:
    print("El nombre de usuario es válido: ", match.group())
else:
    print("El nombre de usuario no es válido", )


# Buscar todas las vocales de una palabra
text = "Hola mundo"
pattern = r"[aeiou]"
matches = re.findall(pattern, text)
print(matches)

# Una Regex para encontrar las palabras man, fan y ban
#  pero ignora el resto
text = "man ran fan ñan ban"
pattern = r"[mfb]an"

matches = re.findall(pattern, text)
print(matches)

# Ejercicio:
# Nos han complicado el asunto, porque ahora hay palabras que encajan pero no empiezan por esas letras.
# Solo queremos las palabras man, fan y ban
text = "omniman fanatico man bandana"
#  \b

text = "22"
pattern = r"[4-9]"

matches = re.findall(pattern, text)
print(matches)


# Ejercicio final con todo lo aprendido
# Mejorar esto: https://www.computerhope.com/jargon/r/regular-expression.png

#  Buscar corner cases que no pasa y arreglarlo:

"lo.que+sea@shopping.online"

# /[\w._%+-]+@[\w.-]+\.[a-zA-Z]{2,4}/]
# text="michael@gov.co.uk"
text = "lo.que+sea@shopping.online"
# Expresión regular para validar un correo electrónico
# Explica la expresión regular
# - `[\w._%+-]+`: Coincide con uno o más caracteres alfanuméricos, guiones bajos, puntos, signos de porcentaje, signos más y guiones.
# - `@`: Coincide con el símbolo arroba.
# - `[\w.-]+`: Coincide con uno o más caracteres alfanuméricos, guiones bajos, puntos y guiones.
# - `\.`: Coincide con un punto literal.
# - `[a-zA-Z]{2,}`: Coincide con dos o más letras mayúsculas o minúsculas.
# - `^` y `$`: Aseguran que la coincidencia sea desde el inicio hasta el final de la cadena.

pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
match = re.search(pattern, text)
if match:
    print("El correo electrónico es válido: ", match.group())
else:
    print("El correo electrónico no es válido", )


# [^]: Coincide con cualquier caracter que no esté dentro de los corchetes
text = "Hola mundo"
pattern = r"[^aeiou]"
matches = re.findall(pattern, text)
print(matches)
