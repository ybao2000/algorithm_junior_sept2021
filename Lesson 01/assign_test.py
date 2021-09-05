i = 1   # integer
i = "test"  # string
print(i)
pi = 3.1415926  # float
b = True    # bool
b2 = False  # bool
z = None

i = 3
j = 5
k = 3*5.0+i+j

# float
a = 0.1
c = a+a+a+a+a+a+a+a+a+a
if c == 1.0:
  print("C is 1: exact compare")
if abs(c-1.0) < 1e-8:
  print("C is 1: tolerance compare")
print(a, c)

z = 2023020223030230203023020220
z1 = 202222222222222222222222222222222222
print(z*z1)

c1 = "happy"
c2 = "holiday"
c = c1 + " " + c2
print(c)
print(f"{c1} {c2}")

b1 = True
b2 = True
print(b1 and b2, b1 or b2, b1^b2)