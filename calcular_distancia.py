import math

def calcular_area(x1, y1, x2, y2, x3, y3):
    return ((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0) 
# toma las coordenadas de tres puntos y calcula el área del triángulo formado por estos puntos 

def esta_dentro(punto1, punto2, punto3, punto4):
    x1, y1 = punto1
    x2, y2 = punto2
    x3, y3 = punto3
    x4, y4 = punto4
    
    area_original = calcular_area(x1, y1, x2, y2, x3, y3)
    area1 = calcular_area(x4, y4, x2, y2, x3, y3)
    area2 = calcular_area(x1, y1, x4, y4, x3, y3)
    area3 = calcular_area(x1, y1, x2, y2, x4, y4)
    
    return area_original == area1 + area2 + area3

def forma_linea(punto1, punto2, punto3):
    x1, y1 = punto1
    x2, y2 = punto2
    x3, y3 = punto3
    
    return (x1 - x2) * (y2 - y3) == (x2 - x3) * (y1 - y2)

def distancia_entre_puntos(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) # para calcular la distancia de los puntos


# Solicita al usuario ingresar las coordenadas del plano cartesiano
punto1 = tuple(map(float, input("Ingresa las coordenadas del primer punto (x, y): ").split(',')))
punto2 = tuple(map(float, input("Ingresa las coordenadas del segundo punto (x, y): ").split(',')))
punto3 = tuple(map(float, input("Ingresa las coordenadas del tercer punto (x, y): ").split(',')))
punto4 = tuple(map(float, input("Ingresa las coordenadas del cuarto punto (x, y): ").split(',')))

# Calcula las distancias del punto 4 a los demas puntos 
distancia_punto4_punto1 = distancia_entre_puntos(punto4, punto1)
distancia_punto4_punto2 = distancia_entre_puntos(punto4, punto2)
distancia_punto4_punto3 = distancia_entre_puntos(punto4, punto3)

# Determina si el cuarto punto está dentro del triángulo
if esta_dentro(punto1, punto2, punto3, punto4):
    print("El cuarto punto está dentro del triángulo formado por los otros tres puntos.")
else:
    print("El cuarto punto no está dentro del triángulo formado por los otros tres puntos.")

# Imprime las distancias 
print(f"Distancia entre el punto 4 y el punto 1: {distancia_punto4_punto1:}")
print(f"Distancia entre el punto 4 y el punto 2: {distancia_punto4_punto2:}")
print(f"Distancia entre el punto 4 y el punto 3: {distancia_punto4_punto3:}")