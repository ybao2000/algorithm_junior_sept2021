N = int(input())
for _ in range(N):
  line = input()
  prev_c = None
  prev_n = 0
  terms = []
  for c in line:
    if prev_c is None:
      prev_c = c  #initialize the char and count
      prev_n = 1
    elif c == prev_c:
      prev_n += 1  #increase the count
    else: #this means you are getting different char
      terms.append(prev_n)
      terms.append(prev_c)
      prev_n = 1 #initialize again
      prev_c = c
  terms.append(prev_n)  # don't forget to append the last one
  terms.append(prev_c)
  print(*terms)