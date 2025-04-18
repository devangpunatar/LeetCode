class Solution:
    def uniqueOccurrences(self, arr):

        count = Counter(arr)
        hashSet = set()

        for i in count.values():
            if i in hashSet:
                return False
            else:
                hashSet.add(i)
        return True