def twoSum(numbers, target):
    start = 0
    end = len(numbers) - 1

    while start < end:
        sum = numbers[start] + numbers[end]
        if sum == target:
            return [start + 1, end + 1]
        else:
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1


print(twoSum([2,7,11,15], 9))