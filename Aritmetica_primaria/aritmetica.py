def contar_acarreos(num1, num2):
    acarreo = 0
    carry_count = 0

    while num1 > 0 or num2 > 0:
        suma = num1 % 10 + num2 % 10 + acarreo
        acarreo = suma // 10
        if acarreo > 0:
            carry_count += 1
        num1 //= 10
        num2 //= 10

    return carry_count

def main():
    while True:
        num1, num2 = map(int, input().split())
        if num1 == 0 and num2 == 0:
            break

        carry_count = contar_acarreos(num1, num2)

        if carry_count == 0:
            print("No lleva operaciones.")
        else:
            print(f"Lleva {carry_count} operacion{'es' if carry_count > 1 else ''}.")

    main()
