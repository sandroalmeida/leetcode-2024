# algorithm is finding the pivot, number where the ascending order from right to left stops
# swap the number before the pivot with the lower number greater than it from the pivot point
# finally reversing the rest of the sub array at right side of the pivot position
def nextPermutation(nums):
    # starting pivot at last position
    pivot = len(nums) - 1

    # moving the pivot until the first element which is not in descending order from previous
    while pivot >= 1 and nums[pivot] <= nums[pivot - 1]:
        pivot -= 1

    # if pivot is not founded its will be zero than we can skip
    if pivot != 0:
        i = len(nums) - 1
        # finding the best number to swap with, greater than pivot
        while nums[i] <= nums[pivot - 1]:
            i -= 1
        # executing the swap
        nums[i], nums[pivot - 1] = nums[pivot - 1], nums[i]

    # reverse sequence from pivot to the end
    l = pivot
    r = len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    return nums


print(nextPermutation([1,7,6,5,1]))

