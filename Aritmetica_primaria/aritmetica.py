import sys

def contar_acarreos(num1, num2):
    
    carry_count = 0
    while num1 > 0 or num2 > 0:
        digit1 = num1 % 10
        digit2 = num2 % 10
        sum_digits = digit1 + digit2 + carry_count
        carry_count = sum_digits // 10
        num1 //= 10
        num2 //= 10

    return carry_count

def main():
    """Reads two numbers, calculates the number of carries, and prints the result."""

    while True:
        try:
            num1_str, num2_str = input().split()
            num1 = int(num1_str)
            num2 = int(num2_str)
        except ValueError:
            print("Invalid input. Please enter two integers.")
            continue

        if num1 == 0 and num2 == 0:
            break

        carry_count = contar_acarreos(num1, num2)

        if carry_count == 0:
            print("No lleva operaciones.")
        else:
            print(f"Lleva {carry_count} operacion{'es' if carry_count > 1 else ''}.")


main()
