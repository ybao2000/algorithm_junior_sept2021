map = {9: 34, 40: 64, 67: 86, 54: 19, 90: 48, 99: 77}
loc = 1
while True:
  step = int(input())
  if step == 0:
    print("You Quit!")
    break
  else:
    if loc + step == 100:
      print("You are now on square 100")
      print("You Win!")
      break
    elif loc + step > 100:
      print(f"You are now on square {loc}")
    else:
      loc = loc + step
      if loc in map:
        loc = map[loc]
      print(f"You are now on square {loc}")        