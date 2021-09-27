s = "Funny cat Garfield dressed as Easter bunny"

# print("".join([a[0] for a in s.split()]).upper())
s1 = s.split()  # split() to split the string into list
s2 = [a[0].upper() for a in s1]  # use list comprehesion to do something
s3 = "-".join(s2) # use join() to glue them together
print(s3)
