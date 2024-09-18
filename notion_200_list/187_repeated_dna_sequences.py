def findRepeatedDnaSequences(s):
    result = []
    if len(s) < 10:
        return result

    l, r = 0, 9
    dna_set = set()
    while r < len(s):
        dna_seq = s[l: r + 1]
        if dna_seq in dna_set and dna_seq not in result:
            result.append(dna_seq)
        l += 1
        r += 1
        dna_set.add(dna_seq)

    return result


print(findRepeatedDnaSequences("AAAAAAAAAAAAA"))
