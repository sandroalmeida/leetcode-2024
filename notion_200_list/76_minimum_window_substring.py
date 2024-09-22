# first solution I think off, not perfect for all edge cases
def minWindow(s, t):
    s_counter = [0] * 26
    t_counter = [0] * 26
    t_set = set()

    for i in t:
        t_counter[ord(i) - ord('A')] += 1
        t_set.add(i)

    output = ""

    l = r = 0
    while r < len(s) and l < (len(s) - len(t)):
        if s[r] in t_set:
            s_counter[ord(s[r]) - ord('A')] += 1
        while (s[l] not in t_set or s_counter[ord(s[l]) - ord('A')] > t_counter[ord(s[l]) - ord('A')]) and l <= r:
            if s[l] in t_set:
                s_counter[ord(s[l]) - ord('A')] -= 1
            l += 1
        if isValid(s_counter, t_counter, t_set):
            if output == "" or len(output) > (r - l + 1):
                output = s[l: r + 1]
        r += 1

    return output


def isValid(s_counter, t_counter, t_set):
    for i in t_set:
        idx = ord(i) - ord('A')
        if s_counter[idx] != t_counter[idx]:
            return False
    return True


print(minWindow("ADOBECODEBANC", "ABC"))