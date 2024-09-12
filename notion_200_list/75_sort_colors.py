def sortColors_mySolution(nums):
    # sorting zeros to the beginning
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[right] == 0:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
        else:
            right -= 1

    # sorting twos to the ending
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] == 2:
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            right -= 1
        else:
            left += 1


def sortColors_optimalSolution(nums):
    left, i, right = 0, 0, len(nums) - 1
    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[right], nums[i] = nums[i], nums[right]
            right -= 1
        else:
            i += 1


nums = [0,0,1,0,1,0,2,1,2,0,1,1,2,1,2]
sortColors_optimalSolution(nums)
print(nums)