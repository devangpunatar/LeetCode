class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {c: i for i, c in enumerate(s)}  # map of last positions
        res = []
        start = end = 0

        for i, c in enumerate(s):
            end = max(end, last_index[c])  # extend window
            if i == end:
                res.append(end - start + 1)  # found a partition
                start = i + 1  # move to next window

        return res
