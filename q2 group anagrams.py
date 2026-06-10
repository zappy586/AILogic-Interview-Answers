def grp_anagrams(strs):
    seen = {}
    result = []
    for i in range(len(strs)):
        for c in strs[i]:
            if c in seen:
                seen[c].append(strs[i])
            else:
                seen[c] = [strs[i]]
    print(seen)
    for i in seen.values():
        result.append(i)
    print(result)
#test
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
grp_anagrams(strs)