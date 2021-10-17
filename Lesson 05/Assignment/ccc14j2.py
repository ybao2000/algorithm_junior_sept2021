V = int(input())
line = input()
n_A = line.count("A")
n_B = line.count("B")

if n_A > n_B:
  print("A")
elif n_A < n_B:
  print("B")
else:
  print("Tie")