# give a list, how to check if it contains duplicate
a = [1, 2, 3, 5, 2]

# way 1, using set, 
# this is not the most efficient way
if len(a) == len(set(a)):
  print("no duplicate")
else:
  print("duplicated")

# way 2, the most efficient way
# given an empty set, if the element is inside, then duplicated
# otherwise, enter the element into the set
def has_duplicate(a):
  s = set()
  for elem in a:
    if elem in s:
      return True
    else:
      s.add(elem)
  return True

if has_duplicate(a):
  print("duplicated")
else:
  print("no duplicate")