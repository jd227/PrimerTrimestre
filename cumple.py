def operacion(edad,precio_play5,precio_juguete):
  dinero_acumulado = 0
  suma_acumulada = 0
  contador = 0
  for i in range(1,edad + 1,2):
          contador = contador + 1
          suma_acumulada = (contador*10)-1
          dinero_acumulado = dinero_acumulado + suma_acumulada
          
  ganancia_juguete = contador * precio_juguete
  dinero_acumulado = dinero_acumulado + ganancia_juguete 
  dinero_acumulado -= precio_play5
  if dinero_acumulado > 0 :

    print("Calculo Acertado!!")
    print("Dinero Sobrante : " ,  dinero_acumulado," Libras")
  else : 
     print("No te alcanza manito : ",dinero_acumulado, "Libras")  

a = int(input("Ingrese la edad de Jeffrey: "))
if a < 1 or a > 90:
    print("La edad debe ser entre 1 y 90.")

b = int(input("Ingrese el precio de la Play5: "))
if b < 150 or b > 10000:
  print("El precio de la Play5 debe estar entre 150 y 10000.")

c = int(input("Ingrese el precio de venta de cada juguete: "))
if c < 2 or c > 40:
  print("El precio de venta de cada juguete debe estar entre 2 y 40.")

operacion(a,b,c)






