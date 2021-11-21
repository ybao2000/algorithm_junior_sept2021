from collections import Counter
# Counter is not built-in (built-in means python already includes it by default)

text = "Hello world"
s = set(text)
print(s)

l = list(text)
print(l)

ic = text.count('l')
print(ic)

# Counter is like a dictionary, key is the character, value is the occurrence
c = Counter(text)
print(c)
print(c['l'])
print("--------------------")
c.update("Merry Christmas")
print(c)
print(c['z'])

# you can use Counter to get the most common letter
print(c.most_common(3))

print("------------------")
for item in c.items():  # keys(), values(), items()
  print(item)
print("------------------")
for elem in c.elements():
  print(elem)