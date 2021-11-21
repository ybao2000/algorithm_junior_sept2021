map = {'b': 'bac', 'c': 'cad', 'd': 'def', 'f': 'feg', 'g': 'geh', 'h': 'hij',
'j': 'jik', 'k': 'kil', 'l': 'lim', 'm': 'mon', 'n': 'nop', 'p': 'poq', 
'q': 'qor', 'r': 'ros', 's': 'sut', 't': 'tuv', 'v': 'vuw', 'w': 'wux',
'x': 'xuy', 'y': 'yuz', 'z': 'zuz'}

s = input()
for c in s:
  if c in map:
    print(map[c], end='')
  else:
    print(c, end='')
print()