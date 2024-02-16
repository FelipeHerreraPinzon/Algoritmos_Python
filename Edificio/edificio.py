import sys

def calcular_edificio_mas_alto(pisos):
    # Contadores para pisos azules y rojos
    azules = 0
    rojos = 0
    
    # Recorre los pisos y cuenta los azules y rojos
    for piso in pisos:
        if piso > 0:
            azules += 1
        else:
            rojos += 1
    
    # Devuelve el mínimo entre azules y rojos, ya que para cada piso se necesita uno del otro color
    return min(azules, rojos)

def main():
    casos = int(sys.stdin.readline().strip())
    for _ in range(casos):
        num_pisos = int(sys.stdin.readline().strip())
        pisos = []
        for _ in range(num_pisos):
            piso = int(sys.stdin.readline().strip())
            pisos.append(piso)
        resultado = calcular_edificio_mas_alto(pisos)
        print(resultado)

if __name__ == "__main__":
    main()
