num_inp = input()
num = int(num_inp)
digits = [c for c in num_inp]
len_digits = len(digits)
nums = [n for n in range(1, 1000000) if len(str(n)) == len_digits and sorted(list(str(n))) == sorted(list(num_inp))]
len_nums = len(nums)
result = 0
for i in range(len_nums):
    if num == nums[i] and i < len_nums - 1:
        result = nums[i + 1]
print(result)