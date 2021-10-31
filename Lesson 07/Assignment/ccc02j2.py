vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

while True:
  word = input()
  if word == "quit!":
    break
  l_word = len(word)
  if l_word > 4 and word.endswith("or") and word[-3] not in vowels:
    print(word[:l_word-2]+"our")
  else:
    print(word)