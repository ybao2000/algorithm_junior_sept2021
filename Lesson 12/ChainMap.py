from collections import ChainMap

# ChainMap is about dictionary
d1 = {'a': 11, 'b': 2, 'c': 3}
d2 = {'a': 4, 'e': 5, 'f': 6}
d3 = {'c': 11, 'd': 12, 'f': 13}
d4 = {}

# what if I want to combine them together
# d = d4 and d2 and d3 and d1 # if there is empty dict, then it will return empty dict, otherwise, it will return the last one
# print(d)

# dd = d1 or d2 or d3 or d4  # this is going to give you the first non-empty dict
# print(dd)
d = {**d1, **d2, **d3, **d4}  # you can use this to combine, this is getting the last value for the same key
print(d)

c = ChainMap(d1, d2, d3, d4)
print(c)
dd = dict(c)
print(dd) # this is getting the first value for the same key