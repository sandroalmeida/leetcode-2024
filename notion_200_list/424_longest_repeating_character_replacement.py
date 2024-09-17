import string


# the first code I came up with
def isValid(str, char_count, k):
    max_count = 0
    for value in char_count.values():
        max_count = max(max_count, value)
    return len(str) - max_count <= k


def characterReplacement(s, k):
    l, r = 0, 0
    char_count = {letter: 0 for letter in string.ascii_uppercase}

    max_length = 0
    while r < len(s):
        aux = char_count[s[r]]
        char_count[s[r]] = aux + 1
        sub_str = s[l:r+1]
        if isValid(sub_str, char_count, k):
            max_length = max(max_length, r - l + 1)
        else:
            l += 1
            aux = char_count[s[l]]
            char_count[s[l]] = aux - 1
        r += 1

    return max_length


# solution from neetcode
def characterReplacement2(s, k):
    char_count = {}
    max_length = 0
    l = 0
    for r in range(len(s)):
        char_count[s[r]] = 1 + char_count.get(s[r], 0)
        if (r - l + 1) - max(char_count.values()) > k:
            char_count[s[l]] -= 1
            l += 1

        max_length = max(max_length, r - l + 1)
    return max_length


print(characterReplacement2("AABABBA", 1))