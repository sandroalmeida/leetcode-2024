def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            l_str = s[left+1:right+1]
            r_str = s[left:right]
            return l_str == l_str[::-1] or r_str == r_str[::-1]
    return True


print(isPalindrome("ebcbbececabbacecbbcbe"))
