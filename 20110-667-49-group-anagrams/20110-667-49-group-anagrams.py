class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping charCount to the list of Anagrams

        for s in strs:
            count = [0] * 26 # a ... z
            for char in s:
                count[ord(char) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())




        