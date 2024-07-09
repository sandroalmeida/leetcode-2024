def containsDuplicate(nums):
    numbers = set()
    for num in nums:
        if (num in numbers):
            return True
        numbers.add(num)
    return False


print(containsDuplicate([1, 2, 3, 2]))
