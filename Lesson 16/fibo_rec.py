N = int(input())

def fibo(n):
  if n == 1 or n == 2:  # base cases
    return 1
  else:
    return fibo(n-1) + fibo(n-2)

print(fibo(N))