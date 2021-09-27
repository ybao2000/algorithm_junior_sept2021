P = int(input())  # P: stopper (whenever > P, stop)
N = int(input())  # N: initial
R = int(input())  # R: rate

day = 0
infect = N
total = N

while total <= P:
  day += 1
  infect *= R
  # infect = N * R**day # although this is correct, but it is slow
  total += infect

print(day)