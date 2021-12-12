n = int(input())
m = int(input())
adjs = []
nouns = []
for i in range(n):
  adjs.append(input())
for i in range(m):
  nouns.append(input())
for i in range(n):
  for j in range(m):
    print(adjs[i], 'as', nouns[j])
