line = input()
s = {"I", "O", "S", "H", "Z", "X", "N"}

all_inside = True
for c in line:
  if c not in s:
    print("NO")
    all_inside = False
    break
# else:
#   print("YES")
if all_inside:
  print("YES")