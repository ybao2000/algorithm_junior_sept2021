s = input()

def is_palindome(a):
  # this is the simplest way, but not the efficient way
  # b = a[::-1]
  # return a == b
  i = 0
  j = len(a)-1
  while i < j:
    if a[i] != a[j]:
      return False
    i += 1
    j -= 1
  return True
    
max_n = 1
len_s = len(s)
for i in range(len_s):
  for j in range(i+1, len_s):
    if is_palindome(s[i:j+1]):
      max_n = max(max_n, j-i+1)
print(max_n)
  
