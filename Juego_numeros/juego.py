def generar_permutaciones(enteros, actual=0):
    if actual == len(enteros) - 1:
        return [[x] for x in enteros]
    
    resultados = []
    for i in range(actual, len(enteros)):
        enteros[actual], enteros[i] = enteros[i], enteros[actual]
        subpermutaciones = generar_permutaciones(enteros, actual + 1)
        for subpermutacion in subpermutaciones:
            resultados.append([enteros[actual]] + subpermutacion)
        enteros[actual], enteros[i] = enteros[i], enteros[actual]
    
    return resultados

def obtener_numero_mas_grande(enteros):
    permutaciones = generar_permutaciones(enteros)
    max_numero = 0
    for perm in permutaciones:
        numero = int(''.join(map(str, perm)))
        max_numero = max(max_numero, numero)
    return max_numero

def main():
    while True:
        n = int(input())
        if n == 0:
            break

        enteros = list(map(int, input().split()))
        resultado = obtener_numero_mas_grande(enteros)
        print(resultado)

if __name__ == "__main__":
    main()


