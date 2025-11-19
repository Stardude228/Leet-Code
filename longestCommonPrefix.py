# longestCommonPrefix completed by Oomat Latipov
def longestCommonPrefix():
    
    strs = ["ab", "a"]
    prefix = ""
    max_prefix_len = min(len(word) for word in strs)

    for j in range(max_prefix_len):
        same = True
        for i in strs:
            if i[j] != strs[0][j]:
                same = False
                break
        if same:
            prefix += strs[0][j]
        else:
            break

    print(prefix)

longestCommonPrefix()

# Leet Code version of longestCommonPrefix
def longestCommonPrefix():
    strs = ["ab", "a"]

    if not strs:
        return ""

    strs.sort()

    first = strs[0]
    last = strs[-1]

    ans = ''

    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            ans += first[i]
        else:
            break

    return ans