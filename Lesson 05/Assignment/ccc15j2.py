text = input()
# we count the symbols
happy = text.count(":-)")
sad = text.count(":-(")

if happy == sad == 0:
  print("none")
elif happy == sad:
  print("unsure")
elif happy > sad:
  print("happy")
else:
  print("sad")