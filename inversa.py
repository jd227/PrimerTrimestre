import random
def crear_matriz(n):
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    for fila in matriz:
        for i in range(len(fila)):
            print(fila[i], end=' ')
        print()
def main():
    n = int(random.randint(1,20))
    matriz = crear_matriz(n)
    matriz_inversa = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            matriz_inversa[i][j] = matriz[j][i]
    imprimir_matriz(matriz)
    print("La matriz inversa es:")
    imprimir_matriz(matriz_inversa)
main()




