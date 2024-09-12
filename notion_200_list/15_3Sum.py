def threeSum(nums):
    nums.sort()
    result = set()
    for i, value in enumerate(nums):
        target = 0 - value
        start = 0
        end = len(nums) - 1
        while start < end:
            if start == i:
                start += 1
                continue
            if end == i:
                end -= 1
                continue
            sum = nums[start] + nums[end]
            if sum == target:
                match = [value, nums[start], nums[end]]
                match.sort()
                result.add(tuple(match))
                start += 1
            elif sum < target:
                start += 1
            else:
                end -= 1

    return result


print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))