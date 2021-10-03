num = int(input())

# use while loop to  print all numbers from num to 0
# FizzBuzz: if the num is multiple of 3, print Fizz,
#           if the num is multiple of 5, print Buzz,
#           if the number is multiple of both 3 and 5, print FizzBuzz
#           otherwise, print the number
i = num # i will be your working variable
while i>=1:
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:
    print(i)
  # if i == 3, get out of the loop, and also don't execute else
  if i== 3: 
    break
  i -= 1
else:
  print("current i:", i)