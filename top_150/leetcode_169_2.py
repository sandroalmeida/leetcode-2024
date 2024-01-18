def majorityElement(nums):
    i = 0
    candidate = None
    while i < len(nums):
        if candidate == None:
            candidate = (nums[i], 1)
        else:
            if nums[i] == candidate[0]:
                candidate = (nums[i], candidate[1] + 1)
            elif nums[i] != candidate[0] and candidate[1] > 1:
                candidate = (candidate[0], candidate[1] - 1)
            else:
                candidate = None
        i += 1
    return candidate[0]


nums = [2, 2, 1, 1, 1, 1, 2]

print(majorityElement(nums))
