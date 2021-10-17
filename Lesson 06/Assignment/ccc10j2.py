a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

def calc_position(f, b, s): # f: forward, b: backward, s: the total steps
  k = s // (f+b)
  ans = k * (f-b)
  rem = s % (f+b) # steps of last round
  if rem <= f:
    return ans + rem
  else:
    return ans + 2 * f - rem

p1 = calc_position(a, b, s)
p2 = calc_position(c, d, s)
if p1 > p2:
  print("Nikky")
elif p1 < p2:
  print("Byron")
else:
  print("Tied")