T = input()
S = input()

for i in range(len(S)):
  # iterate through all cyclic shift
  if S in T:
    print("yes")
    break
  S = S[1:] + S[0]  # move the first letter to the end
else:
  print("no")