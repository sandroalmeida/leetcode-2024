# Example 1:
# Input: s1 = "abcdebdde", s2 = "bde"
# Output: "bcde"
# Explanation:
# "bcde" is the answer because it occurs before "bdde" which has the same length.
# "deb" is not a smaller window because the elements of s2 in the window must occur in order.
def minWindow(s1, s2):
    # the idea is looping throughout s1 looking for the final character of s2
    # we start by the final character because it will be the limit for a minimum window
    # when we find this character we start another loop with two pointers
    # the idea is comparing the s1 characters from that point in reverse order with s2
    # each time the characters match we can move s2 pointer
    # if s2 pointer achieve -1 means all s2 characters have had matched, so we have one solution
    # the solutions need to be compare and keep the smaller one
    # and the external loop can continue looking for the next match for the final character of s2
    result = ""
    for i in range(len(s1)):
        if s1[i] == s2[-1]:
            p1 = i
            p2 = len(s2) - 1
            while p1 >= 0 and p2 >= 0:
                if s1[p1] == s2[p2]:
                    p2 -= 1
                p1 -= 1
                if p2 < 0:
                    if result == "" or (i - p1) < len(result):
                        result = s1[p1 + 1: i + 1]
    return result


print(minWindow("hpsrhgogezyfrwfrejytjkzvgpjnqil", "sgy"))
# solution works well for small subsets but got a time exceed on leetcode
# keep as future reference, maybe using some way of storing results and
# avoiding looping some sections again ?!?!

