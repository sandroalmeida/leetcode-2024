def isPalindrome(s):
    def check(left, right, s, extra):
        while left < right:
            if s[left] != s[right]:
                if extra:
                    return False
                else:
                    return check(left+1, right, s, True) or check(left, right-1, s, True)
            else:
                left += 1
                right -= 1
        return True
    return check(0, len(s) - 1, s, False)


print(isPalindrome("ABCDBA"))
