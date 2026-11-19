s = input().lower()
print(sum(c in "aeiou" for c in s))
