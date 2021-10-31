while True:
  C = int(input())
  if C == 0:
    break
  a = 1
  b = C
  k = 2
  while k*k <= C:
    if C % k ==0:   # only consider k as C's factor
      a = k
      b = C//k
    k += 1
  p = 2 * (a + b)
  print(f"Minimum perimeter is {p} with dimensions {a} x {b}")