dirs = []
streets = ['HOME']
while True:
  direction = input()
  if direction == 'L':
    dirs.append('RIGHT')
  else:
    dirs.append('LEFT')
  street = input()
  if street == 'SCHOOL':
    break
  streets.append(street)
dirs = dirs[::-1]
streets = streets[::-1]
for i in range(len(dirs)):
  if i == len(dirs)-1:
    print(f"Turn {dirs[i]} into your HOME.")
  else:
    print(f"Turn {dirs[i]} onto {streets[i]} street.")
