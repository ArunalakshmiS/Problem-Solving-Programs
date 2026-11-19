a = list(map(int, input().split()))
u = sorted(set(a), reverse=True)
print(u[1] if len(u) > 1 else "No distinct second largest")
