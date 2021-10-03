vals = input().split()
n = int(vals[0])
k = int(vals[1])
half = (n+1)//2
if k <= half:
  print(2*k-1)
else:
  print((k-half)*2)