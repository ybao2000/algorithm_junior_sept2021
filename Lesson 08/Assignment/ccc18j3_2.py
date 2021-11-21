a = [int(val) for val in input().split()]
n = len(a) + 1
b = [0] * n # intialize the position of all cites
for i in range(n-1):
  b[i+1] = b[i] + a[i]

for i in range(n):
  diffs = []
  for k in range(n):
    diffs.append(abs(b[k]-b[i]))
  print(*diffs)