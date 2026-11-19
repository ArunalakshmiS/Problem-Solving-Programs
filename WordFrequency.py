from collections import Counter
words = input().lower().split()
print(dict(Counter(words)))
