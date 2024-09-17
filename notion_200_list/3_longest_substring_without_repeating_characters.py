# create 2 pointers L and R positioning them at 0 index
# check if value of right pointer is on the dict
# if not add R pointer and check for max
# if it is on dict
# remove from dict
# add L pointer and check again
# loop ends when right pointer surpass length

def lengthOfLongestSubstring(s):
    l, r = 0, 0
    distinct_set = set()

    max_length = 0
    while r < len(s):
        if distinct_set.__contains__(s[r]):
            distinct_set.remove(s[l])
            l += 1
        else:
            distinct_set.add(s[r])
            r += 1
            max_length = max(max_length, r - l)

    return max_length


print(lengthOfLongestSubstring("pwwkew"))