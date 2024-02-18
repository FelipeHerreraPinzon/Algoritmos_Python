import sys

def max_edificio(pisos):
 
    azules = 0
    rojos = 0
    
    pisos.sort(key=abs, reverse=True)
    
    for piso in pisos:
        if piso > 0:  # Azul
            if rojos == azules:
                azules += 1
        else:  # Rojo
            if azules == rojos + 1:
                rojos += 1
    
    return azules + rojos

def main():
    casos = int(sys.stdin.readline().strip())
    for _ in range(casos):
        num_pisos = int(sys.stdin.readline().strip())
        pisos = [int(sys.stdin.readline().strip()) for _ in range(num_pisos)]
        resultado = max_edificio(pisos)
        print(resultado)

if __name__ == "__main__":
    main()
