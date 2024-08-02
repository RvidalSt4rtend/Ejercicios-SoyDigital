import numpy as np

def ejercicio1(matrix):
    if not isinstance(matrix, list) or not all(isinstance(i, list) for i in matrix):
        print("Ingrese Una Matriz de Forma Correcta")
        return
    
    length_matrix = len(matrix[0])
    if not all(len(row) == length_matrix for row in matrix):
        print("Todas las filas de la matriz deben tener la misma longitud")
        return
    
    matrix = np.array(matrix).flatten()
    unique, counts = np.unique(matrix, return_counts=True)

    unique = np.sum(counts == 1)
    repeat = np.sum(counts > 1)

    print(f"Únicos: {unique}")
    print(f"Repetidos: {repeat}")

    return [unique, repeat]


print("Ejemplo 1")
ejercicio1([[2, 1, 3], [4, 5, 2], [6, 6, 6]])
print("=====================================")
print("Ejemplo 2")
ejercicio1([[1, 2, 3], [4, 5, 6], [7, 8, 8]])
print("=====================================")
print("Ejemplo 3")
ejercicio1([[1,2,3],[1]])
