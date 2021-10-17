a, b, c, d, e = "A", "B", "C", "D", "E"

# define a function to do the nasty work
def operate(B, n):
  global a, b, c, d, e
  for _ in range(n):
    if B == 1:
      # move the first to the end
      a, b, c, d, e = b, c, d, e, a #left side is the new ones, right side is the original ones
    elif B == 2:
      # move the last to the first
      a, b, c, d, e = e, a, b, c, d
    elif B == 3:
      # swap the first two
      a, b = b, a

# you need infinite while loop
while True:
  B = int(input())
  n  = int(input())
  if B == 4:
    break
  operate(B, n)

print(a, b, c, d, e)

