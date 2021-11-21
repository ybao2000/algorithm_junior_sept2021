n = int(input())
a = 100
d = 100
for _ in range(n):
  points = input().split()
  pa = int(points[0])
  pd = int(points[1])
  if pa < pd:
    # a loses pd points
    a -= pd
  elif pa > pd:
    # b loses pa points
    d -= pa
print(a)
print(d)
  