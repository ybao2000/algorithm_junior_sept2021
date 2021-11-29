n = int(input())

# calculate 1+2+3+...+n
# total = 0
# for i in range(1,n+1):  # brute
#   total += i  
# print(total)

total = n * (n+1) // 2
print(total)