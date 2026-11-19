a, b = map(int, input().split())
for n in range(max(2,a), b+1):
    if all(n % i for i in range(2, int(n**0.5)+1)):
        print(n, end=" ")
