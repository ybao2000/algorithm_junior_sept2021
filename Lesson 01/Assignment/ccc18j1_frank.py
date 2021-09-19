d1 = int(input())
d2 = int(input())
d3 = int(input())
d4 = int(input())

c1 = (d1 == 8 or d1 == 9)
c2 = (d4 == 8 or d4 == 9)
c3 = (d2 == d3)

if c1 and c2 and c3:
  print("ignore")
else:
  print("answer")
