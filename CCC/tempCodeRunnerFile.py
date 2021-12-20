if h < 10:
  str_h = '0' + str(h)
else:
  str_h = str(h)
if m < 10:
  str_m = '0' + str(m)
else:
  str_m = str(m)

print(str_h + ':' + str_m)