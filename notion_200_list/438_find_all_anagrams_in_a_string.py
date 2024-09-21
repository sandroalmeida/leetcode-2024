# Example 1:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]
# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".
from collections import Counter

# first solution I come up with
def findAnagrams(s, p):

    anan_dict = {}
    for item in p:
        anan_dict[item] = anan_dict.get(item, 0) + 1

    result = []
    l = 0
    while l <= (len(s) - len(p)):
        if s[l] in anan_dict and l + len(p) <= len(s):
            map_check = anan_dict.copy()
            for r in range(l + len(p) - 1, -1 , -1):
                if s[r] in map_check and map_check.get(s[r]) > 0:
                    map_check[s[r]] = map_check.get(s[r]) - 1
                else:
                    break
            if sum(map_check.values()) == 0:
                result.append(l)
        l += 1

    return result

# The first solution is not optimal because of the internal loop
# we don't need an internal loop because we are adding one new char from right and remove one from left all the time
# is easy update the same map by using these values and comparing
# also no copy of map is need, we can copy the partial s map directly with the p map
def findAnagrams2(s, p):

    result = []
    map_p = Counter(p)
    map_s = Counter()

    for l in range(len(s)):
        # Add right position to the counter s
        map_s[s[l]] += 1

        # Removing left position from the counter s
        if l >= len(p):
            if map_s[s[l - len(p)]] == 1:
                del map_s[s[l - len(p)]]
            else:
                map_s[s[l - len(p)]] -= 1

        # comparing maps
        if map_p == map_s:
            result.append(l - len(p) + 1)

    return result


print(findAnagrams2("abab", "ab"))