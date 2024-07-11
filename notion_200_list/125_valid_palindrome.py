import re
def isPalindrome(s):
    clean_string = re.sub(r'[^a-zA-Z0-9]+', '', s).lower()
    right = 0
    left = len(clean_string) - 1
    while(right < left):
        if(clean_string[right] != clean_string[left]):
            return False
        else:
            right += 1
            left -= 1
    return True


print(isPalindrome("A man, a plan, a canal: Panama"))
