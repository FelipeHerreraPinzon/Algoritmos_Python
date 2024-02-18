def maxima_altura_edificio(pisos):
    max_altura = 0
    altura_actual = 0
    color_anterior = None
    
    for piso in pisos:
        if (piso > 0 and color_anterior != 'azul') or (piso < 0 and color_anterior != 'rojo'):
            altura_actual = 0
        
        if piso > 0:
            color_actual = 'azul'
        else:
            color_actual = 'rojo'
        
        if color_actual != color_anterior:
            altura_actual = 0
        
        altura_actual += 1
        max_altura = max(max_altura, altura_actual)
        
        color_anterior = color_actual
    
    return max_altura

def main():
    casos = int(input().strip())
    for _ in range(casos):
        num_pisos = int(input().strip()) 
        pisos = [int(input().strip()) for _ in range(num_pisos)]
        print(maxima_altura_edificio(pisos))  

if __name__ == "__main__":
    main()
