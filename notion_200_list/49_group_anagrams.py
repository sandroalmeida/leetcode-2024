# my first solution without looking anything
def groupAnagrams(strs):
    # build a hash function for a word
    def getHash(chars):
        hash = ""
        for c in chars:
            hash = hash + str(ord(c))
        return hash
    # dict should be hash value as key and list of string matching the hash
    dict = {}
    for item in strs:
        hash = getHash(sorted(item))
        if hash in dict:
            dict[hash].append(item)
        else:
            dict[hash] = [item]
    # iterate the dict to form the final result
    result = []
    for item in dict.values():
        result.append(item)

    return result


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
