import math

def calcular():
  print("hola, bien venido.")
  print("que quieres hacer? ")
  print("1. suma")
  print("2. resta")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. potencia")
  print("6. porcentaje")
  print("7. logaritmo")
  print("8. raiz")

  requerido=int(input("cual es tu respuesta: "))
#bloque de comparaciones según la elección del usuario
  if requerido == 7 or requerido == 8:
        numero1= float(input("entra el primer numero: "))
  else:
      numero1= float(input("entra el primer numero: "))
      numero2= float(input("entra el segundo numero: "))
      pass
  if requerido == 1:
        print("El resultado es:", numero1 + numero2)
  elif requerido == 2: 
        print("El resultado es:", numero1 - numero2)
  elif   requerido == 3:
        print("El resultado es:", numero1 * numero2)
  elif requerido == 4:
        if numero2 != 0:
            print("El resultado es:", numero1 / numero2)
        else:
            print("No se puede dividir entre cero.")
  elif requerido == 5:
        print("El resultado es:", numero1 ** numero2)
  elif requerido == 6:
        print("El resultado es:", (numero1 * numero2) / 100)
  elif requerido == 7:
        print("El resultado es:", math.log10(numero1))
  elif requerido == 8:
        print(f"El resultado la raiz de {numero1} es:", math.sqrt(numero1))
   

calcular()