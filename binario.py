def comienzo():


  numero = int(input("Introduce un número decimal: "))
  lista_binario = convertir_a_binario(numero)
  print("El número binario es:", lista_binario)
  numero_decimal = int("".join(map(str, lista_binario)), 2)
  print("El número binario corresponde al número decimal:", numero_decimal)

def convertir_a_binario(numero):

  lista_binario = []
  while numero != 0:
    residuo = numero % 2
    lista_binario.append(residuo)
    numero //= 2
  if len(lista_binario) < 3:
    
    lista_binario.extend([0] * (3 - len(lista_binario)))
  return lista_binario[::-1]




comienzo()