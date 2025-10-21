n = int(input())

nums = []

for _ in range(n):
    nums.append(int(input()))

nums.sort()

index = len(nums) // 2

if nums[index] < (len(nums) - index):
    while index < len(nums) and nums[index] < (len(nums) - index):
        index += 1
    print(nums[index - 1])
else:
    while nums[index] > (len(nums) - index):
        index -= 1
    print(nums[index])
