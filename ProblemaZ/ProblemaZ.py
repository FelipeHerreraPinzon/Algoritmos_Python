import sys
#Programa para calcular la cantidad y suma de numeros 
#pares en una lista de numeros

def procesarNumeros(numeros):
    respuestas = [0,0]
    for i in range (0,len(numeros)):
        if(numeros[i]%2==0):
            respuestas[0] += 1
            respuestas[1] +=numeros[i]
    return respuestas

def main():
    linea = sys.stdin.readline()
    ncasos = int(linea)
    linea = sys.stdin.readline()
    for i in range(0,ncasos):
        numeros = [int(num) for num in linea.split()]
        respuesta = procesarNumeros(numeros)
        print(str(respuesta[0]) + " " + str(respuesta[1]))
        linea = sys.stdin.readline()
    
main()