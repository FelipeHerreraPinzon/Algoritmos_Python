import sys

def numero_mas_grande(numeros):
    numeros.sort(key=lambda x: str(x)*10, reverse=True)
    numero_mas_grande = ''.join(map(str, numeros))
    return int(numero_mas_grande)

def main():
    while True:
        n = int(sys.stdin.readline().strip())
        if n == 0:
            break
        numeros = list(map(int, sys.stdin.readline().split()))
        resultado = numero_mas_grande(numeros)
        print(resultado)

main()
