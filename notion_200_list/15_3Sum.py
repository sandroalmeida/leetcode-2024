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


def threeSumWithHash(nums):
    result = set()
    for i in range(len(nums)):
        sub_array = nums[:i] + nums[i+1:]
        partials = twoSum(sub_array, 0 - nums[i])
        for v1, v2 in partials:
            sum_res = [nums[i]] + [v1, v2]
            sum_res.sort()
            result.add((sum_res[0], sum_res[1], sum_res[2]))
    return result


def twoSum(sub_nums, target):
    result = set()
    dict = {}
    for idx, value in enumerate(sub_nums):
        pair = dict.get(value)
        if pair is not None:
            if value < pair:
                result.add((value, pair))
            else:
                result.add((pair, value))
        dict[target - value] = value
    return result


def threeSumOptimal(nums):
    result = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            sum = a + nums[l] + nums[r]
            if sum > 0:
                r -= 1
            elif sum < 0:
                l += 1
            else:
                result.append([a, nums[l], nums[r]])
                l += 1
                while nums[l-1] == nums[l] and l < r:
                    l += 1
    return result


print(threeSumOptimal([-1,0,1,2,-1,-4]))