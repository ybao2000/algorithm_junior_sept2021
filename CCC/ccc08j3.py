def find_loc(c):
  if c == ' ':
    return (4, 2)
  elif c == '-':
    return (4, 3)
  elif c == '.':
    return (4, 4)
  else:
    d = ord(c) - ord('A') # get the ascii code ofr che character
    return (d//6, d%6)

s = input()
prev_loc = (0,  0) 
moves = 0
for c in s:
  loc = find_loc(c)
  moves += abs(loc[0]-prev_loc[0]) + abs(loc[1]-prev_loc[1])
  prev_loc = loc

moves += abs(loc[0]-4) + abs(loc[1]-5)
print(moves)