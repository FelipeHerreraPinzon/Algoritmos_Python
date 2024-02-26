import sys

def ordenar(numeros):
    numeros = list(map(int, numeros.split()))
    n = len(numeros)

    for i in range(n):
        for j in range(n-i-1):
            if numeros[j] > numeros[j+1]:
                numeros[j], numeros[j+1] = numeros[j+1], numeros[j]
    print(numeros)            

def main():
    entrada = sys.stdin.readline()
    ordenar(entrada)    

main()    
