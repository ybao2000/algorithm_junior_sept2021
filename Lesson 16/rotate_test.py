a = [[4, 3, 1],
[6, 5, 2],
[9, 7, 3]]

# clock wise rotate
a = list(zip(*a[::-1]))   # * is unpack
for ai in a:
  print(*ai)