h = int(input())
M = int(input())

for t in range(1, M+1):
  # A = -6 * t**4 + h * t**3 + 2 * t **2 + t
  t2 = t*t
  t3 = t2*t
  t4 = t3*t
  A = -6 * t4 + h * t3 + 2 *t2 + t
  if A<=0:
    # this the answer we want
    print("The balloon first touches ground at hour:")
    print(t)
    break
else:
  print("The balloon does not touch ground in the given time.")
