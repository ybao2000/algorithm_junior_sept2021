A = int(input())
B = int(input())
if A > 0 and B > 0:
    print("1")
if A < 0 and B > 0:
    print("2")
if A > 0 and B < 0:
    print("4")
if A < 0 and B < 0:
    print("3")