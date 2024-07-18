def longestConsecutive(nums):
    numSet = set(nums)
    maxSeq = 0
    for num in nums:
        # checking if num is a start of a sequence
        if (num - 1) not in numSet:
            count = 1
            # checking size of the sequence
            while (num + count) in numSet:
                count += 1
            maxSeq = max(maxSeq, count)
    return maxSeq


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
