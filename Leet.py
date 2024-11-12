nums = [5,4,3,2,1]

for i in range(len(nums)):
    step1 = i + 1
    step2 = step1 + 1
    if step2 >= len(nums):
        print(nums[i - 1], nums[step1 - 1], nums[step2 - 1])
        print(False)
        break
    elif nums[i] < nums[step1] and nums[step1] < nums[step2]:
        print(True)
        break
