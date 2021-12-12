a = [3, -4, 2, -1, 4, 5, -2, -3, 7, -2, -3]

# find the sub array that has the maximum sum
# you can use Kadane's algorith, O(n)
max_sum_all = 0
max_sum_end_at_i = 0
for i in range(len(a)):
  max_sum_end_at_i = max(max_sum_end_at_i+a[i], a[i])
  max_sum_all = max(max_sum_all, max_sum_end_at_i)
print(max_sum_all)
