def calculate_min_distance(relatives):
    relatives.sort()  # Ordena las calles donde viven los parientes
    median = relatives[len(relatives) // 2]  # Calcula la mediana de las calles

    # Calcula la suma mínima de distancias desde la casa óptima hasta cada pariente
    total_distance = sum(abs(x - median) for x in relatives)

    return total_distance

def main():
    # Lee el número de casos de prueba
    num_cases = int(input())

    for _ in range(num_cases):
        # Lee el número de parientes y las calles donde viven
        num_relatives, *relative_streets = map(int, input().split())

        # Calcula y muestra la suma mínima de distancias para el caso actual
        result = calculate_min_distance(relative_streets)
        print(result)

if __name__ == "__main__":
    main()
