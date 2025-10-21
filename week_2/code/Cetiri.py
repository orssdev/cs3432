input_nums = input().split()
nums = [int(n) for n in input_nums]

nums.sort()

diff1 = abs(nums[0] - nums[1])
diff2 = abs(nums[1] - nums[2])

if diff1 == diff2:
    print (nums[2] + diff1)
elif diff1 > diff2:
    print (nums[0] + diff2)
else:
    print(nums[2] - diff1)