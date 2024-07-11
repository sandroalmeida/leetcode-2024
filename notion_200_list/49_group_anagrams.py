# my first solution without looking anything
def groupAnagrams(strs):
    # dict with sorted value as key and list of string matching the hash
    dict = {}
    for item in strs:
        sorted_item = "".join(sorted(item))
        if sorted_item in dict:
            dict[sorted_item].append(item)
        else:
            dict[sorted_item] = [item]
    # iterate the dict to form the final result
    result = []
    for item in dict.values():
        result.append(item)

    return result


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
