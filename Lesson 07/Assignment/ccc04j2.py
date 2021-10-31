a = int(input())
b = int(input())
# lcm for 2, 4, 3, 5 is 60
for i in range(a, b+1, 60): # start from a, every time increase 60, b is included
  print(f"All positions change in year {i}")