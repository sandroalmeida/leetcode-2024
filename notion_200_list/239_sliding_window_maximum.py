import collections


# this problem has a lot of tricks to be solved in this linear optimal way
# first using deque for storing always bigger values on the beginning
# second using the queue with the indexes for removing left position easier (number comparison can cause issues)
# third condition for removing left is a bit counterintuitive
def maxSlidingWindow(nums, k):
    output = []
    q = collections.deque()
    l = r = 0

    while r < len(nums):
        # remove elements smaller than r value from the queue if them exists
        while q and nums[q[-1]] < nums[r]:
            q.pop()
        q.append(r)

        # remove left val from window
        if l > q[0]:
            q.popleft()

        # starting adding output and increment l after reach window size
        if (r + 1) >= k:
            output.append(nums[q[0]])
            l += 1

        r += 1

    return output


print(maxSlidingWindow([1,3,1,2,0,5], 3))