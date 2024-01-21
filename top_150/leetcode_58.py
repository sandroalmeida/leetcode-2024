# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal
# substring
#  consisting of non-space characters only.
# Example 1:
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:
# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.

# Constraints:
# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

def lengthOfLastWord(s):
    return len(s.split()[-1])


def lengthOfLastWord2(s):
    s = s.strip()
    lastIndex = len(s) - 1
    while lastIndex >= 0:
        if s[lastIndex] == " ":
            return len(s) - 1 - lastIndex
        lastIndex -= 1
    return len(s)


s = "    day"
print(lengthOfLastWord(s))
print(lengthOfLastWord2(s))
