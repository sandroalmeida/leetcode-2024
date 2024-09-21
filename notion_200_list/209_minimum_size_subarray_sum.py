def minSubArrayLen(target, nums):
    l, r = 0, 0
    current_sum = 0
    min_len = len(nums) + 1

    while r < len(nums):
        current_sum += nums[r]
        while current_sum >= target:
            min_len = min(r - l + 1, min_len)
            current_sum -= nums[l]
            l += 1
        r += 1
    if min_len == len(nums) + 1:
        min_len = 0

    return min_len


print(minSubArrayLen(7, [2,3,1,2,4,3]))