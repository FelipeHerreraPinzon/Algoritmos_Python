import sys

def calcular_suma_distancias(parientes):
    parientes.sort()
    n = len(parientes)
    distancia_minima = float('inf')

    # Calcula la distancia mínima desde la ubicación de la casa de Vito a cada pariente
    for i in range(n):
        suma_distancias = sum(abs(pariente - parientes[i]) for pariente in parientes)
        distancia_minima = min(distancia_minima, suma_distancias)

    return distancia_minima

def main():
    casos_prueba = int(sys.stdin.readline().strip())
    for _ in range(casos_prueba):
        entrada = sys.stdin.readline().split()
        num_parientes = int(entrada[0])
        ubicaciones_parientes = list(map(int, entrada[1:]))
        resultado = calcular_suma_distancias(ubicaciones_parientes)
        print(resultado)

main()

