t = (1, 2, 3) # tuple is using round brackets
l = [1, 2, 3] # list is using square brackets
s = {1, 2, 3} # set is using curly brackets
d = {'apple': 1, "banana": 2, "cherry": 3} # dictinary is also using curly brackets

t = ((1, 2), (2, 3), (3, 4)) # tuple of tuple
t2 = ([1, 2], [2, 3], [3, 4]) # tuple of list
print(t[0][0])
print(t2[0][0])
t3 = t2[0]
t3[0] = 11;
print(t3)

l = [[1, 2, 3], [2, 3, 4], [3, 4, 5]] # list of list
l2 = [(1, 2, 3), (2, 3, 4), (3, 4, 5)] # list of tuple

d2 = {1: [1, 2, 3], 2: [2, 3, 4], 3: [3, 4, 5]} # dictionary, key is int, values is list
d2 = {(1, 2): (3, 4), (1, 3): (4, 5)}
print(d2[(1, 2)]) # tuple can be used as key

# d3 = {[1, 2]: [3, 4], [1, 3]: [4, 5]} # list cannot be key because list is mutable
# print(d3[1, 2])