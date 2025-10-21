try:    
    while True:
        nums = [int(n) for n in input().split()]
        diffs = []
        for i in range(len(nums) - 1):
            diffs.append(abs(nums[i] - nums[i + 1]))
        if all(diffs[i] <= diffs[i+1] for i in range(len(diffs) - 1)) or all(diffs[i] >= diffs[i+1] for i in range(len(diffs) - 1)):
            print('Jolly')
        else:
            print('Not jolly')
except:
    pass