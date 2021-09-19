A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
F = int(input())
G = A * 3 + B * 2 + C * 1
H = D * 3 + E * 2 + F * 1
if G > H:
    print("A")
elif H > G:
    print("B")
else:
    print("T")