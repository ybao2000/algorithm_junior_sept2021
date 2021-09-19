mark = int(input())
if mark < 0 or mark > 100: # this is to ensure mark is always [0, 100]
  print("wrong mark")
elif mark >= 85:
  print("grade is A")
elif mark >= 70:
  print("grade is B")
elif mark >= 50:
  print("grade is C")
else:
  print("grade is F")
