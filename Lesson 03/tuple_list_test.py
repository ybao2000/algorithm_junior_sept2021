# what is the difference between tuple and list

t = (1, 2, 3, 4, 5)

l = [1, 2, 3, 4, 5]

# tuple is immutable (cannot be changed), list is mutable (can be changed)
# how to change list?
# for the list, you can change element using index
l[0] = 10;
# for the list, you can also append a new member
l.append(50)
# you can also delete something
l.pop(0)
print(l)

# tuple cannot be changed!!!
# for tuple, no update, no add, no delete
print(t[0])

# then why using tuple!!!
# one important case is you can use tuple as key of dictionary, 
# you cannot use list as key of dictionary
