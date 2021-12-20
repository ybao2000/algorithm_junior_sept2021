N = int(input())

a = []  # 2D list
for _ in range(N):
  a.append(input().split())

def valid(a):
  a1 = int(a[0][0])
  a2 = int(a[-1][0])
  a3 = int(a[0][-1])
  a4 = int(a[-1][-1])
  return a1 < a2 and a1 < a3 and a1 < a4

while not valid(a):
  a = list(zip(*a[::-1])) # clock-wise rotate

for ai in a:
  print(*ai)
