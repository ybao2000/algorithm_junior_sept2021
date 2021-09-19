n = int(input())
total = 0
for _ in range(n):
  vals = input().split()
  n1 = int(vals[0])
  n2 = int(vals[1])
  n3 = int(vals[2])
  if n1+n2+n3 >= 2:
    total += 1    # total = total + 1
print(total)
