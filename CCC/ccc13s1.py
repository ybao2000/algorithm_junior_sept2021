Y = int(input())
while True:
  Y += 1
  sY = str(Y)
  if len(sY) == len(set(sY)):
    print(Y)
    break