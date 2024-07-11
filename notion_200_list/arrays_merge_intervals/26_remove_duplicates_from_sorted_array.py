def removeDuplicates(nums):
    # [1,2,3,3,4,5,5,6,7,8]
    # k = 8 length 10
    # storage current value and current position
    # iterate through the array from second position checking if it is the desirable value (means > current)
    # if condition checked swap and update position and current
    # if condition doesn't check continue looping with updating
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
