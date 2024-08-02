# first solution I came out with
def employeeFreeTime(schedule):
    # add all intervals in an unique list
    combined_list = []
    for intervals in schedule:
        combined_list = combined_list + intervals

    # sort this list
    combined_list.sort()

    # merge the overlapping intervals inside this list
    merged_list = [combined_list[0]]
    for start, end in combined_list[1:]:
        if start <= merged_list[-1][1]:
            merged_list[-1][1] = max(merged_list[-1][1], end)
        else:
            merged_list.append([start, end])

    # loop through the list picking up the gaps
    res = []
    for i in range(1, len(merged_list)):
        res.append([merged_list[i-1][1], merged_list[i][0]])

    return res


def employeeFreeTime2(schedule):
    # add all intervals in an unique list
    combined_list = []
    for intervals in schedule:
        combined_list = combined_list + intervals

    # sort this list
    combined_list.sort()

    res = []
    # by tracking the last end we can find the free times
    # if the next interval starts after the last end we found a free time
    # this is the reason of defining end with first interval and start the loop from the second
    current_end = combined_list[0][1]
    for interval in combined_list[1:]:
        if interval[0] > current_end:
           res.append([current_end, interval[0]])
        current_end = max(current_end, interval[1])

    return res


print(employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))
print(employeeFreeTime2([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]))

