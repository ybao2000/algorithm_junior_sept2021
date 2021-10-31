m = int(input())
n = int(input())
total = 0
map = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
for num in range(m, n+1):
  a = str(num)
  idx_1 = 0
  idx_2 = len(a)-1
  while idx_1 <= idx_2:
      c1 = a[idx_1]
      c2 = a[idx_2]
      if c1 not in map or c2 not in map or c1 != map[c2]:
        break
      idx_1 += 1
      idx_2 -= 1
  else:
    total += 1
print(total) 