def leastInterval(tasks, n):

    # creating a dict with all the characters and frequencies
    frequencies = {}
    for task in tasks:
        frequencies[task] = frequencies.get(task, 0) + 1

     # sorting the dict
    sorted_frequencies = sorted(frequencies.items(), key=lambda item:item[1], reverse=True)

    # finding the max frequent item for calculating the idle time considering only this item
    max_frequency = sorted_frequencies[0][1]
    # calculating idle time if only this item was present
    idle_time = (max_frequency - 1) * n
    # removing this item from frequencies
    sorted_frequencies.pop(0)

    # looping until the map is empty or idle become negative
    while len(sorted_frequencies) > 0 and idle_time > 0:
        # filling up idle spots with current max frequent item
        idle_time -= min(max_frequency - 1, sorted_frequencies[0][1])
        # excluding current max frequent
        sorted_frequencies.pop(0)

    # if idle become negative changed it to zero
    idle_time = max(0, idle_time)

    # result will be len tasks and final idle
    return len(tasks) + idle_time


print(leastInterval(["A", "A", "A", "B", "B", "C", "C", "D"], 2))

