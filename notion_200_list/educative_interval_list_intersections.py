# create two pointers to go through each list
# create a while loop until one of the pointers reach the end
# if current interval from first list is smaller than current interval from second increment pointer 1
# same for pointer 2
# smaller interval means not in the range of intersection, or end of one interval smaller than start of other interval
# if both conditions are not true the intersection exists
# at this case insert the intersection on result and move both pointers
def intervalIntersection(firstList, secondList):
    p1, p2 = 0, 0
    res = []
    while p1 < len(firstList) and p2 < len(secondList):
        currentFirst = firstList[p1]
        currentSecond = secondList[p2]
        if currentFirst[1] < currentSecond[0]:
            p1 += 1
            continue
        elif currentSecond[1] < currentFirst[0]:
            p2 += 1
            continue
        else:
            newInterval = [max(currentFirst[0], currentSecond[0]), min(currentFirst[1], currentSecond[1])]
            res.append(newInterval)
            if newInterval[1] == currentFirst[1]:
                p1 += 1
            else:
                p2 += 1
    return res


print(intervalIntersection([[0,2],[5,10],[13,23],[24,25]], [[1,5],[8,12],[15,24],[25,26]]))
