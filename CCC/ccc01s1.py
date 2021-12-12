cards = input()
idx_D = cards.find('D')
idx_H = cards.find('H')
idx_S = cards.find('S')
list_C = list(cards[1:idx_D])
list_D = list(cards[idx_D+1:idx_H])
list_H = list(cards[idx_H+1:idx_S])
list_S = list(cards[idx_S+1:])

def count_points(list_card):
  points = 0
  if 'A' in list_card:
    points += 4
  if 'K' in list_card:
    points += 3
  if 'Q' in list_card:
    points += 2
  if 'J' in list_card:
    points += 1
  if len(list_card) == 0:
    points += 3     
  if len(list_card) == 1:
    points += 2       
  if len(list_card) == 2:
    points += 1  
  return points

def print_format(title, list_card, points):
  txt = title + " " + " ".join(list_card)
  print(txt.ljust(28, ' '), points)

# we are going to define a function for the points
points_C = count_points(list_C)
points_D = count_points(list_D)
points_H = count_points(list_H)
points_S = count_points(list_S)
print("Cards Dealt\t\tPoints")
print_format("Clubs", list_C, points_C)
print_format("Diamonds", list_D, points_D)
print_format("Hearts", list_H, points_H)
print_format("Spades", list_S, points_S)
final = f"Total {points_C+points_D+points_H+points_S}"
print(final.rjust(30, ' '))