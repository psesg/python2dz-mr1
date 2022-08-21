
def permutations(s):
    if not s:
        return []
    partial = []
    partial.append(s[0])
    for i in range(1, len(s)):
        for j in reversed(range(len(partial))):
            curr = partial.pop(j)
            for k in range(len(curr) + 1):
                partial.append(curr[:k] + s[i] + curr[k:])
    return partial

test = "PycharmPr"
pm = permutations(test)
print len(pm)