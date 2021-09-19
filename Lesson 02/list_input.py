# read to read in the list of int
# 1 2 3 4 5 56
# a = input().split()
# print(a)
# you use list comprehension
a = [int(val) for val in input().split()]
print(a)