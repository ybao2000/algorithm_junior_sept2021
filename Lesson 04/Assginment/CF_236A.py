line = input()
s = set(line) # convert string into set, list
if len(s) % 2 == 0:  # even
  print("CHAT WITH HER!")
else:
  print("IGNORE HIM!")