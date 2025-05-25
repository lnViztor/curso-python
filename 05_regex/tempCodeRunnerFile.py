import re
text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la"  # Hola, H0la, H$la

found = re.findall(pattern, text)

if (found):
    print(found)
else:
    print("No se ha encontrado el patrón")