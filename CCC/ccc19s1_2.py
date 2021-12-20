n1, n2, n3, n4 = 1, 2, 3, 4
vals = input()
nH = vals.count('H')
nV = vals.count('V')

# sequence doesn't matter
# if you have 2 H/V flips, they will cancel each other

if nH % 2 == 1: # horizontal flip
  n1, n2, n3, n4 = n3, n4, n1, n2
if nV % 2 == 1:
  n1, n2, n3, n4 = n2, n1, n4, n3

print(f"{n1} {n2}")
print(f"{n3} {n4}")