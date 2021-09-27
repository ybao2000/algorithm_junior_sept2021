# container is a collection of multiple items
# tuple, list, set, dictionary: linear container
# linear containers: you can either use index or key to get the value
# tuple, list: you can use index, index is a 0-based sequence number
# t = (1, 2, 3, 4)
# t1 = t[1] # second item
# t2 = t[-1] # the last one
# t3 = t[-2] # the second last one
# print(t1, t2, t3)
l = [1, 2, 3, 4]  
# everything from tuple applies to list
l1 = l[1]
l2 = l[-1]
l3 = l[-2]
print(l1, l2, l3)
# a big question: what is the difference between tuple and list
# tuple: immutable, list: mutable
# why should we use tuple?
# tuple:memory efficient, but that's not the most important reason
# nowdays, memory is not big problem
# the essential point to use tuple is: tuple can be used as key, list cannot!!!
