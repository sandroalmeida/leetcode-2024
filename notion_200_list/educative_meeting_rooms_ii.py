import heapq


def minMeetingRooms(intervals):
    intervals.sort()
    rooms = 1
    min_heap = []
    heapq.heappush(min_heap, intervals[0][1])
    for start, end in intervals[1:]:
        if start >= min_heap[0]:
            heapq.heappop(min_heap)
        else:
            rooms += 1
        heapq.heappush(min_heap, end)
    return rooms


print(minMeetingRooms([[7,10],[2,4]]))