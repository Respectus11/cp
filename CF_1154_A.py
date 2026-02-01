
nums = list(map(int, input().split()))
nums.sort()
total = nums[3]   
a = total - nums[2]
b = total - nums[1]
c = total - nums[0]

print(a, b, c)
