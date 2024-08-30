#1
#Toma 2 matrices de igual tamaño (matrices bidimensionales)
#Devuelva una nueva matriz que sea la suma de las 2 matrices originales
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

filas = len(matrix1)
columnas = len(matrix1[0])
matrixres = [[0 for _ in range(columnas)] for _ in range(filas)]

for i in range(filas):
    for j in range(columnas):
        matrixres[i][j] = matrix1[i][j] + matrix2[i][j]
print("La matriz resultante de la suma es:")
for fila in matrixres:
    print(fila)


#2
#Multiplique 2 matrices de tamaño adecuado.
#Para multiplicar matrices, el número de columnas de la primera debe coincidir con el número de filas de la segunda
# Definimos las dos matrices
matrixa = [
    [1, 2, 3],
    [4, 5, 6]
]
matrixb = [
    [7, 8],
    [9, 10],
    [11, 12]
]

filasa = len(matrixa)
columnasa = len(matrixa[0])
columnasb = len(matrixb[0])
resumatrix = [[0 for _ in range(columnasb)] for _ in range(filasa)]

for i in range(filasa):
    for j in range(columnasb):
        for k in range(columnasa):
            resumatrix[i][j] += matrixa[i][k] * matrixb[k][j]
print("La matriz resultante de la multiplicación es:")
for fila in resumatrix:
    print(fila)

#3
#Tome una matriz y devuelva su transpuesta (intercambiar filas por columnas)
# Definimos la matriz original
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrixtrans = [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]
print("La matriz transpuesta es:")
for fila in matrixtrans:
    print(fila)


#4
#Un cuadrado mágico es una matriz en la que la suma de cada fila, columna y diagonal es la misma.
#Escribe un programa que determine si una matriz dada es un cuadrado mágico.
def is_magic_square(matrix):
    n = len(matrix)
    sum_row = sum(matrix[0])
    sum_diag1 = 0
    sum_diag2 = 0

    for i in range(n):
        if sum(matrix[i]) != sum_row:
            return False
        sum_diag1 += matrix[i][i]
        sum_diag2 += matrix[i][n - i - 1]

    for j in range(n):
        if sum(matrix[i][j] for i in range(n)) != sum_row:
            return False

    if sum_diag1 != sum_row or sum_diag2 != sum_row:
        return False

    return True

# Matrices a evaluar
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[9, 8, 7],
           [6, 5, 4],
           [3, 2, 1]]

matrix3 = [[2, 7, 6],
           [9, 5, 1],
           [4, 3, 8]]

# Imprimir matrices
print(f'Esta es la primera matriz:\n{matrix1}')
print(f'Esta es la segunda matriz:\n{matrix2}')
print(f'Esta es la tercera matriz:\n{matrix3}')
print()

# Verificar si son cuadrados mágicos
print(f"¿Matriz 1 es un cuadrado mágico?: {is_magic_square(matrix1)}")
print(f"¿Matriz 2 es un cuadrado mágico?: {is_magic_square(matrix2)}")
print(f"¿Matriz 3 es un cuadrado mágico?: {is_magic_square(matrix3)}")

print("Fin del programa")