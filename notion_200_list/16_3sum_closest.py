def threeSumClosest(nums, target):
    nums.sort()
    closest_sum = float('inf')

    for i, a in enumerate(nums):
        l, r = i + 1, len(nums) - 1
        while l < r:
            current_sum = a + nums[l] + nums[r]
            if abs(target - closest_sum) > abs(target - current_sum):
                closest_sum = current_sum
            if current_sum > target:
                r -= 1
            elif current_sum < target:
                l += 1
            else:
                return current_sum
    return closest_sum


print(threeSumClosest([-1,2,1,-4], 1))
print(threeSumClosest([0,0,0], 1))