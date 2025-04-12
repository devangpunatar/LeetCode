class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        hashMap = {} # map each char to their first and last index
        for i, c in enumerate(s):
            if c not in hashMap:
                hashMap[c] = [i, i]
            else:
                hashMap[c][1] = i

        res.append(hashMap[s[0]])
        last_end = hashMap[s[0]][1]
    
        for start, end in list(hashMap.values())[1:]:
            last_end = res[-1][1]
            if start <= last_end:
                res[-1][1] = max(end, last_end)
            else:
                res.append([start, end])
        size = []
        for l, r in res:
            size.append(r - l + 1)

        return size