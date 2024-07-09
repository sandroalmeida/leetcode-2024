def isPalindrome(s):
    right = 0
    left = len(s) - 1
    exclusions = True

    while right < left:
        if s[right] == s[left]:
            right += 1
            left -= 1
        elif s[right] == s[left - 1] and exclusions:
            exclusions = False
            right += 1
            left -= 2
        elif s[right + 1] == s[left] and exclusions:
            exclusions = False
            right += 2
            left -= 1
        else:
            return False
    return True


print(isPalindrome("ABCPBA"))
