# words = input().split("WUB")
# stripped = [word for word in words if word != '']
# result = str.join(" ", stripped)
# print(result)

words = input().split("WUB")
concate = str.join(" ", words)
# print(concate)
items = concate.strip().split() # this can remove additional spaces
result = str.join(" ", items);
print(result)