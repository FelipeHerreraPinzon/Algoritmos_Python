import sys

def contar__acarreos(num1, num2):
    carry_count = 0
    carry = 0
    while num1 > 0 or num2 > 0:
        dig1 = num1 % 10
        dig2 = num2 % 10
        suma = dig1 + dig2 + carry
        if suma >= 10:
            carry_count += 1
            carry = 1
        else:
            carry = 0
        num1 //= 10
        num2 //= 10
    return carry_count

def main():
    while True:
        num1_str, num2_str = sys.stdin.readline().split()
        num1 = int(num1_str)
        num2 = int(num2_str)
        if num1 == 0 and num2 == 0:
            break
        operaciones_acarreo = contar__acarreos(num1, num2)
        if operaciones_acarreo == 0:
            print("No lleva operaciones.")
        elif operaciones_acarreo == 1:
            print("Lleva 1 operacion.")
        else:
            print(f"Lleva {operaciones_acarreo} operaciones.")


main()
