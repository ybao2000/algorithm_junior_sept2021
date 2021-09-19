A = int(input())
B = int(input())
C = int(input())
D = int(input())
E=0
if A==8 or A==9:
    E+=1
if C==B:
    E+=1
if D==8 or D==9:
    E+=1
if E==3:
    print("ignore")
else:
    print("answer")