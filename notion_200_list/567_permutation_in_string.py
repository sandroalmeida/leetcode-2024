from collections import Counter


def checkInclusion(s1, s2):
    l, r = 0, len(s1) - 1
    # creating initial window dict
    s2_windows_dict = Counter(s2[l:r+1])
    # creating s2 dict
    s1_dict = Counter(s1)

    while r < len(s2):
        # comparing window and s1 dict
        if s2_windows_dict == s1_dict:
            return True
        else:
            # updating l pointer and window dict
            s2_value = s2_windows_dict.get(s2[l])
            if s2_value == 1:
                s2_windows_dict.pop(s2[l])
            else:
                s2_windows_dict[s2[l]] = s2_value - 1
            l += 1
            # updating r pointer and window dict
            r += 1
            if r < len(s2):
                s2_windows_dict[s2[r]] = s2_windows_dict.get(s2[r], 0) + 1

    return False


print(checkInclusion("cbaa", "aabaccaaacba"))
