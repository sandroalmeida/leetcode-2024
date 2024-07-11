def isAnagram(s, t):
    # testing edge case first
    if len(s) != len(t):
        return False
    dict = {}
    # creating a new dict based on the string s
    for l in s:
        if l in dict:
            dict[l] = dict[l] + 1
        else:
            dict[l] = 1
    # checking the dict against string t
    for l in t:
        if l in dict:
            if dict[l] == 1:
                del dict[l]
            else:
                dict[l] = dict[l] - 1
        else:
            return False
    return len(dict) == 0


print(isAnagram("anagram", "nagaram"))
