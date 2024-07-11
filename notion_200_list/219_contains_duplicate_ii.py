def containsNearbyDuplicate(nums, k):
    dict = {}
    for idx, number in enumerate(nums):
        if number in dict and abs(dict[number] - idx) <= k:
            return True
        else:
            dict[number] = idx
    return False


print(containsNearbyDuplicate([1,2,3,1], 3))
print(containsNearbyDuplicate([1,2,3,1,2,3], 2))