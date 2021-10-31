m = int(input())
n = int(input())
total = 0
map = {0: 0, 1: 1, 8: 8, 6: 9, 9: 6}  # this is for rotation
for num in range(m, n+1):
  a = num
  b = 0
  while a > 0:
    rem = a % 10
    if rem not in map:
      break
    else:
      b  = b * 10 + map[rem]
    a = a // 10
  else:
    if num == b:
      total += 1
print(total)