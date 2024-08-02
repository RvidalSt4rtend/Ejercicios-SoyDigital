def ejercico2(n):
    if not isinstance(n, int):
        raise ValueError("El valor ingresado no es un número entero")
    if n <= 0 or n >=10**6:
        raise ValueError("El valor ingresado debe ser un número natural positivo")
    
    pairs = [(i, n - i) for i in range(1, (n//2)+1)]
    print(pairs)
    return pairs

print("Ejemplo 1")
ejercico2(5)
print("=====================================")
print("Ejemplo 2")
ejercico2(10)
