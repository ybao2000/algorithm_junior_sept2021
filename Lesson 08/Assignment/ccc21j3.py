while True: # infinity loop
  val = input()
  if val == '99999':
    break
  first = int(val[0])
  second = int(val[1])
  steps = val[2:]
  if first+second > 0:
    if (first+second) % 2 == 0:
      direction = "right"
    else:
      direction = "left"
  print(f"{direction} {steps}")