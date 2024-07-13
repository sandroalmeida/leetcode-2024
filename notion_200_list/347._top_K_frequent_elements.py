def topKFrequent(nums, k):
    # creating count dictionary
    count = {}
    for n in nums:
        count[n] = 1 + count.get(n, 0)

    # creating frequency array
    freq = [[] for i in range(len(nums) + 1)]
    for n, c in count.items():
        freq[c].append(n)

    # iterating from the end (most frequent) to the beginning
    # appending k times to the result
    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res


print(topKFrequent([1,1,1,2,2,3,4], 2))