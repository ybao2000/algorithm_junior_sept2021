import time
n = int(input())
start = time.time()
total = sum(range(1, n + 1))
end = time.time()
print(total, end-start)
