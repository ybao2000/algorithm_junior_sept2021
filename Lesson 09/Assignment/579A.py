x = int(input())
b = bin(x)
total = 0
for c in b:
  if c == '1':
    total += 1
print(total)