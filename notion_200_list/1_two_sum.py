def twoSum(nums, target):
    dict = {}
    for idx, num in enumerate(nums):
        if num in dict:
            return [dict[num], idx]
        else:
            dict[target - num] = idx


print(twoSum([1,2,3,4,5], 9))
