# solution one:
# creating a new array, updating with values from n in the right place
# copying from original array
def rotate(nums, k):
    n = len(nums)
    copy = [0] * n
    for i in range(n):
        copy[(i + k) % n] = nums[i]

    nums[:] = copy


# [1,2,3,4,5] = 3 times
# if we reverse the entire array [5,4,3,2,1]
# than reverse the first k elements [4,5,3,2,1]
# than reverse the second k elements [4,5,1,2,3]
# rotation will be concluded
def rotateInPlace(nums, k):
    k = k % len(nums)
    reverseInPlace(nums, 0, len(nums) - 1)
    reverseInPlace(nums, 0, k - 1)
    reverseInPlace(nums, k, len(nums) - 1)


def reverseInPlace(nums, l, r):
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


nums1 = [-1,-100,3,99]
nums2 = [1,2,3,4,5,6,7]

rotateInPlace(nums1, 2)
rotateInPlace(nums2, 3)

print(nums1)
print(nums2)
