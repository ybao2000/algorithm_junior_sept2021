amounts = [100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000]
n = int(input())
for _ in range(n):
  a = int(input()) 
  amounts[a-1] = 0  # don't forget to offset by 1
offer = int(input())
avg = sum(amounts)/(10-n) # n is the removed number, remaining is 10 - n
if offer > avg:
  print("deal")
else:
  print("no deal")
