# Given a pattern and a string s, find if s follows the same pattern.
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
# Example 1:
# Input: pattern = "abba", s = "dog cat cat dog"
# Output: true
# Example 2:
# Input: pattern = "abba", s = "dog cat cat fish"
# Output: false
# Example 3:
# Input: pattern = "aaaa", s = "dog cat cat dog"
# Output: false
# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.

def wordPattern(pattern, s):
    pattern_s_dict = {}
    s_pattern_dict = {}
    words = s.split()
    if len(pattern) != len(words):
        return False
    for i in range(len(pattern)):
        letter = pattern[i]
        word = words[i]
        dict_letter = s_pattern_dict.get(word)
        dict_word = pattern_s_dict.get(letter)
        if dict_letter == None and dict_word == None:
            pattern_s_dict[letter] = word
            s_pattern_dict[word] = letter
        elif dict_letter != None and dict_word != word:
            return False
        elif dict_word != None and dict_letter != letter:
            return False

    return True


pattern = "abba"
s = "dog cat cat dog"

print(wordPattern(pattern, s))
