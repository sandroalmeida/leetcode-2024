def reverseWords(s):
    words = s.split()
    result = ""
    for i in range(len(words) - 1, -1, -1):
        result = result + " " + words[i]

    return result.strip()

def reverseWordsTwoPointers(s):
    result = []
    s = s.strip()
    if len(s) == 1:
        return s
    left, right = len(s) - 1, len(s) - 1
    while left >= 0:
        if (s[left] == " " or left == 0) and left != right:
            word = s[left:right + 1]
            no_spaces = word.strip()
            if no_spaces != "":
                result.append(no_spaces)
            right = left
        else:
            left -= 1
    return " ".join(result).strip()


print(reverseWordsTwoPointers("this is the   last    exercise today   "))
print(reverseWords("this is the last exercise today"))