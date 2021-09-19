import time
# read in an interger, and sum up from 1 to that number
# while loop
n = int(input())
i = 1 # this is the variable starting from 1 to n
total = 0
start = time.time()
while i<=n:
  total += i
  i += 1    # don't forget to increase the i
end = time.time()
print(total, end-start)
