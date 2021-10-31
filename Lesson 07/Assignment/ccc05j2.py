def count_factors(n):
  ic = 2
  # for k in range(2, n):
  #   if n % k == 0:
  #     ic += 1
  k = 2
  while k*k <= n: # you can stop at sqrt(n)
    if n % k == 0:    # this is a factor
      if k*k == n:
        ic +=1
      else:
        ic += 2
    k += 1
  return ic;

a = int(input())
b = int(input())
total = 0
for i in range(a, b+1): # b is included
  num = count_factors(i)
  if num == 4:
    total += 1
print(f"The number of RSA numbers between {a} and {b} is {total}")