from collections import defaultdict

# my first solution without looking anything
def groupAnagrams(strs):
    # dict with sorted value as key and list of string matching the hash
    res = defaultdict(list)
    for item in strs:
        sorted_item = "".join(sorted(item))
        res[sorted_item].append(item)

    return res.values()

#neetcode solution
def groupAnagrams2(strs):
    res = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)

    return res.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"]))
