test = int(input())

num_pad = [
    [1, 2, 3],
    [3, 4, 5],
    [7, 8, 9],
    [-1, 0, -1]
]

num_pad_loc = [(3,2), (0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]

for _ in range(test):
    nums = [int(c) for c in input()]
    x, y = num_pad_loc[nums[0]]
    result = [nums[0]]
    nums = nums[1:]
    for n in nums:
        if y < 3 and x < 3:
            if num_pad[x][y + 1] == nums[0] or abs(num_pad[x][y + 1] - nums[0]) < abs(num_pad[x + 1][y] - nums[0]):
                result.append(num_pad[x][y + 1])
                y += 1
            elif num_pad[x + 1][y] == nums[0] or abs(num_pad[x + 1][y] - nums[0]) < abs(num_pad[x][y + 1] - nums[0]):
                result.append(num_pad[x + 1][y])
                x += 1
        nums = nums[1:]
    print(result)