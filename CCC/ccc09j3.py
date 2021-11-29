def normalize(t):
  if t < 0:
    return t + 2400
  elif t >= 2400:
    return t-2400
  return t

t_o = int(input())
print(f"{t_o} in Ottawa")
t_v = normalize(t_o-300)
print(f"{t_v} in Victoria")
t_e = normalize(t_o-200)
print(f"{t_e} in Edmonton")
t_w = normalize(t_o-100)
print(f"{t_w} in Winnipeg")
print(f"{t_o} in Toronto")
t_h = normalize(t_o+100)
print(f"{t_h} in Halifax")
minute = t_o % 100
if minute < 30:
  t_s = normalize(t_o+130)
else:
  hour = t_o // 100
  t_s = normalize(hour *100 + 200 + minute - 30 )
print(f"{t_s} in St. John's")