import time
n = int(input())
total = 0
start = time.time()
for i in range(1, n+1): # n+1 is excluded
  total += i
end = time.time()
print(total, end-start)
