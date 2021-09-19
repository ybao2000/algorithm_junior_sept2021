l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]  # members can be duplidated
# first, do you know how to sum them up?
print(sum(l))
# how to count the numbers
print(len(l))
# here is a tough one: how to sum up all the even positions
t = l[::2]
print(t, sum(t))
# here is even tougher one, I want to square the even positions and sum them up
total = 0
# for i in range(len(l)):
#   if i % 2 == 0:
#     total += l[i]*l[i]
for i, num in enumerate(l):
  if i % 2 == 0:
    total += num * num
print(total)

# list comprehesion
# t =sum([val*val for val in l[::2]])
t = sum([val*val for key, val in enumerate(l) if key%2==0])
print(t)

# here is another problem, I want square of all even number and sum them up
total = 0
for num in l:
  if num % 2 == 0:
    total += num * num
print(total)

t = [val*val for val in l if val % 2 == 0]
print(t)