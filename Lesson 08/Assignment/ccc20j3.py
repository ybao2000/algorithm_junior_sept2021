N = int(input())
x_min, y_min, x_max, y_max = 101, 101, 0, 0
for _ in range(N):
  vals = input().split(',')
  x = int(vals[0])
  y = int(vals[1])
  # if x < x_min:
  #   x_min =x 
  # if x > x_max:
  #   x_max = x
  # if y < y_min:
  #   y_min = y
  # if y > y_max:
  #   y_max = y
  x_min = min(x_min, x)
  y_min = min(y_min, y)
  x_max = max(x_max, x)
  y_max = max(y_max, y)
print(f"{x_min-1},{y_min-1}") # {} allows expression
print(f"{x_max+1},{y_max+1}")
