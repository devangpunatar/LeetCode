class Solution:
    def alienOrder(self, words: List[str]) -> str:
        graph = {}
        for word in words:
            for c in word:
                graph[c] = []
        
        for i in range(1, len(words)):
            w1, w2 = words[i - 1], words[i]
            minL = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minL] == w2[:minL]:
                return ""
            for j in range(minL):
                if w1[j] != w2[j]:
                    graph[w1[j]].append(w2[j])
                    break
            
        visited = set()
        visiting = set()
        res = []    

        def dfs(node):
            if node in visiting:
                return False
            if node in visited:
                return True
            visiting.add(node)
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            visiting.remove(node)
            visited.add(node)
            res.append(node)
            return True

        for c in graph:
            if c not in visited:
                if not dfs(c):
                    return ""

        return "".join(reversed(res))