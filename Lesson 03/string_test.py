# string is a special tuple
# string is immutable!

# s = "Hello world"
# print(s[0])
# # s[0] = "T"
# s = 'T' + s[1:]
# print(s)

ms = """Twinkle twinkle little star
How I wonder what you are"""

# print(ms)
print(ms[5:])   # get a substring, starting from 5
print(ms[:10])    # get the first 10 characters, index 10 is excluded
print(ms[5:10])   # get the substring, index starting from 5, ending at 10 (exluceed)
print(ms[::-1])   # this is to reverse everything
print(ms[10:5:-1])