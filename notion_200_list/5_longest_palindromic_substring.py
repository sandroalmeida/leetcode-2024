def longestPalindrome(s):
    max_palindrome = ""
    for i in range(len(s)):
        # odd length
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_palindrome = s[left:right+1]
            if len(current_palindrome) > len(max_palindrome):
                max_palindrome = current_palindrome
            left -= 1
            right += 1

        # even length
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            current_palindrome = s[left:right + 1]
            if len(current_palindrome) > len(max_palindrome):
                max_palindrome = current_palindrome
            left -= 1
            right += 1
    return max_palindrome


print(longestPalindrome("cbbd"))
