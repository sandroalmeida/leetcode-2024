# OBS At the Educative prompt the array was sorted, but not at Leetcode, so it was added the sorted step to the solution
def merge(intervals):
    # validating edge case intervals equals 0 or 1 don't need to process
    if len(intervals) <= 1:
        return intervals

    # sorting intervals by the first digit, only possible to merge if intervals is sorted that way
    intervals.sort()

    # creating the result array and adding the first interval
    res = [intervals[0]]

    # extracting start and end for each interval starting at second position (idx == 1)
    for start, end in intervals[1:]:
        # checking if start number of the current interval is smaller or equal to start number of last result interval
        if start <= res[-1][1]:
            # if True update the last position by the max value making the merge of the intervals in the result
            res[-1][1] = max(end, res[-1][1])
        else:
            # if False append the current array to result and continue checking the next interval
            res.append([start, end])

    return res


print(merge([[1,3],[2,6],[8,10],[15,18]]))
