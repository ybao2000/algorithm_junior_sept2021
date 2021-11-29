def gcd(a, b):  #brute force: efficient
  x = max(a, b)
  y = min(a, b)
  while y > 0:
    r = x % y
    x = y
    y = r
  return x


vals = input().split()
a = int(vals[0])
b = int(vals[1])
print(gcd(a, b))