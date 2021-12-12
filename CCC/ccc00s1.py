quarters = int(input())
m1 = int(input())
m2 = int(input())
m3 = int(input())
times = 0

while quarters > 0:
  # one quarter, one play
  # starting from m1
  times += 1  
  quarters -= 1
  m1 += 1
  if m1 == 35:
    quarters += 30
    m1 = 0
  if quarters == 0:
    break
  # go to m2
  times += 1  
  quarters -= 1
  m2 += 1
  if m2 == 100:
    quarters += 60
    m2 = 0
  if quarters == 0:
    break  
  # go to m3
  times += 1  
  quarters -= 1
  m3 += 1
  if m3 == 10:
    quarters += 9
    m3 = 0

print(f"Martha plays {times} times before going broke.")   
