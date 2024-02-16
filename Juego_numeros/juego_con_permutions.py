from itertools import permutations

def obtener_numero_mas_grande(enteros):
    max_numero = 0
    for perm in permutations(enteros):
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


main()
