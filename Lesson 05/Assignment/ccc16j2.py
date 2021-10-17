# 2D matrix
# I am going to use list of list
squares = []
for _ in range(4):
  vals = [int(val) for val in input().split()]
  squares.append(vals)

# here we will use set to check if all sums are the same
# the items in set is unique
s = set()
for i in range(4):
  s1 = 0
  s2 = 0
  for j in range(4):
    s1 += squares[i][j]   # adding up all cells for row i
    s2 += squares[j][i]   # adding up all cells for column i
  s.add(s1)
  s.add(s2)

if len(s) == 1:
  print("magic")
else:
  print("not magic")