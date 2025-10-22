n = int(input())
nums = [int(x) for x in input().split()]

if nums[0] % 3 == 0:
    j1 = nums[0] // 3
    j2 = nums[1] - (2 * j1)
    j3 = nums[n - 1] // 3
print(j1, j2, j3)
