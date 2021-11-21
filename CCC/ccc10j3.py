v = [0, 0]

def map(x):
  if x == 'A':
    return 0
  else:
    return 1

while True:
  vals = input().split()
  op = int(vals[0])
  if op == 7:
    break
  else:
    x = vals[1]
    ix = map(x)
    if op == 1:
      v[ix] = int(vals[2])
    elif op == 2:
      print(v[ix])
    else:
      y = vals[2]
      iy = map(y)
      if op == 3:
        v[ix] = v[ix] + v[iy]
      elif op == 4:
        v[ix] = v[ix] * v[iy]
      elif op == 5:
        v[ix] = v[ix] - v[iy]
      elif op == 6:
        v[ix] = v[ix]//v[iy]
