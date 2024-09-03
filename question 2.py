def is_fibonacci_number(n):
    a, b = 0, 1
    while b <= n:
        if b == n:
            return True
        a, b = b, a + b
    return False


num = int(input("Informe um número: "))
if is_fibonacci_number(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
