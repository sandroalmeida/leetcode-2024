def insert(intervals, newInterval):
    res = []
    # looping through out all intervals
    for i in range(len(intervals)):
        # first checking if new interval end number is smaller than start number of current interval
        # this means the interval can be inserted at the beginning and rest of intervals can be combined with it
        # this works if loop is in the first or subsequence intervals
        if newInterval[1] < intervals[i][0]:
            res.append(newInterval)
            return res + intervals[i:]
        # if above condition is not True check if start number of new interval is bigger than end number of current interval
        # this means the current interval can be added to the result because don't need to merge with new interval
        # loop will continue checking new interval against other subsequent intervals
        elif newInterval[0] > intervals[i][1]:
            res.append(intervals[i])
        # when both above conditions are not True means a merge is needed
        # so the new interval is created by using max of both intervals, new and current
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    # at the end of the loop is possible the return of the first condition was not reached
    # so the new interval need to be added by the end of the array and then returned
    res.append(newInterval)
    return res


# second solution is a little easy to intuit, the main idea is insert all intervals smaller than new one
# then when merge is need do the merge operation until the new interval surpass the merged one
# then add the merged one
# finally insert all the intervals after the merge operation
def insert2(intervals, newInterval):
    res = []
    idx = 0

    # inserting all intervals smaller and not overlapping with the new interval
    while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
        res.append(intervals[idx])
        idx += 1

    # merging overlapping intervals
    while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
        newInterval[0] = min(intervals[idx][0], newInterval[0])
        newInterval[1] = max(intervals[idx][1], newInterval[1])
        idx += 1

    # after creating the new merged interval appending it
    res.append(newInterval)

    while idx < len(intervals):
        res.append(intervals[idx])
        idx += 1

    return res


print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
print(insert2([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
