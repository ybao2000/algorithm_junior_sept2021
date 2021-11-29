def gcd(a, b):  #brute force: inefficient
  x = max(a, b)
  y = min(a, b)
  # you want to start from min(a, b) => 1
  for i in range(y, 0, -1):
    if x % i == 0 and y % i == 0:
      return i


vals = input().split()
a = int(vals[0])
b = int(vals[1])
print(gcd(a, b))