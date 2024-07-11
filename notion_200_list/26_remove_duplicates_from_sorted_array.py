def removeDuplicates(nums):
    current = nums[0]
    position = 1
    for i in range(1, len(nums)):
        number = nums[i]
        if number > current:
            nums[position] = number
            position += 1
            current = number
    return position


print(removeDuplicates([1,2,3,3,4,5,5,6,7,8]))
