# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

def canConstruct(ransomNote, magazine):
    char_dict = {}
    for letter in magazine:
        if char_dict.get(letter) == None:
            char_dict[letter] = 1
        else:
            char_dict[letter] = char_dict.get(letter) + 1

    for letter in ransomNote:
        if char_dict.get(letter) == None:
            return False
        else:
            current = char_dict.get(letter)
            if current == 1:
                del char_dict[letter]
            else:
                char_dict[letter] = char_dict.get(letter) - 1
    return True


ransomNote = "aabb"
magazine = "aab"

print(canConstruct(ransomNote, magazine))
