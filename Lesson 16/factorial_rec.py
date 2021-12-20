n = int(input())

# recurrcen formula
# f(n) = f(n-1) * n

def fact(n):
  if n == 1: 
    return 1
  else:
    return fact(n-1) * n

print(fact(n))