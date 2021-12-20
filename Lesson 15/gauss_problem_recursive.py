n = int(input())

def gauss_sum(n):
  if n == 1:  # base case 
    return 1
  else:
    # recursive formula: s(n) = s(n-1) + n
    return gauss_sum(n-1)+n

print(gauss_sum(n))