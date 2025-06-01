import re
#text="michael@gov.co.uk"
text="lo.que+sea@shopping.online"
pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
match = re.search(pattern, text)
if match:
    print("El correo electrónico es válido: ", match.group())
else:
    print("El correo electrónico no es válido", )