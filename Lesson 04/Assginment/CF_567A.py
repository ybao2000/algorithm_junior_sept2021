n = int(input())
x = [int(val) for val in input().split()]
for i in range(n):
  if i == 0:
    # this is the start
    print(x[i+1]-x[i], x[n-1]-x[i])
  elif i == n-1:
    print(x[i]-x[i-1], x[i]-x[0])
  else:
    ln = x[i]-x[i-1]
    rn = x[i+1]-x[i]
    h = x[i] - x[0]
    e = x[n-1]-x[i]
    print(min(ln, rn), max(h, e))