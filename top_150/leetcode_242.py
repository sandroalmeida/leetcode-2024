# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
# Follow up: What if the inputs contain Unicode characters?
# How would you adapt your solution to such a case?

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    letters_map = {}
    for letter in s:
        value = letters_map.get(letter)
        if value == None:
            letters_map[letter] = 1
        else:
            letters_map[letter] = value + 1
    for letter in t:
        value = letters_map.get(letter)
        if value == None or value == 0:
            return False
        else:
            letters_map[letter] = value - 1
    return True


s = "rat"
t = "car"

print(isAnagram(s, t))
