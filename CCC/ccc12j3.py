k = int(input())

# a list of list
a = [['*', 'x', '*'], 
[' ', 'x', 'x'],
['*', ' ', '*']
]
for i in range(3):
  for _ in range(k):
    for j in range(3):
      print(a[i][j]*k, end='')
    print()