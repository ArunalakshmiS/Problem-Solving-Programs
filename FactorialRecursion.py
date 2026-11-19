def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)

n = int(input())
print(factorial(n))
