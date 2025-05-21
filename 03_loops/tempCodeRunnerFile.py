def calcular_total(precio_base, descuento=0, impuesto=0):
  """Calcula el precio total aplicando descuento e impuesto"""
  precio_con_descuento = precio_base - (precio_base * descuento)
  precio_final = precio_con_descuento + (precio_con_descuento * impuesto)
  return round(precio_final)

print(calcular_total(100, 0.1, 0.16)) # precio_base=100, descuento=10%, impuesto=20%