a = 'hello world' # please convert it into some numbers a => 1, b=>2, .... space a separator
# b = ord(a)
# print(a, b)

# [85121215, 231518124]
a2 = a.split()
b2 = []
for word in a2:  # iterate through the words
  nums = []
  for c in word:  # iterate through the char
    d = ord(c) - ord('a') + 1
    nums.append(str(d))
  b2.append(int("".join(nums)))
print(*b2)
# print(*b2, sep="-")