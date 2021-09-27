# a = [1, 2, 4, 5, 6, 26]

# # i want a tring "abdefz"
# # b = 13
# # y = ord(x) - ord('a') + 1
# # y -1 = ord(x) - ord('a')
# # ord(x) - ord('a) = y - 1
# # ord(x) = ord('a) + y - 1
# # c = chr(ord('a') + b - 1)
# # print(b, c)

# b = [chr(ord('a')+val-1) for val in a]
# print("".join(b))

nums = [1, 2, 4, 5, 6, 26]
chars = "".join([chr(i + 96) for i in nums])
print(chars)
