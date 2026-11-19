from collections import Counter
s = input().replace(" ", "")
print([c for c,n in Counter(s).items() if n > 1])
