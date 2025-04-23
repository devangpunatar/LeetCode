class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1
        
        bank.append(startGene)
        geneMap = collections.defaultdict(list)
        for gene in bank:
            for i in range(8):
                pattern = gene[:i] + '*' + gene[i + 1:]
                geneMap[pattern].append(gene)

        visited = set([startGene])
        q = deque([startGene])
        res = 0
        while q:
            for _ in range(len(q)):
                gene = q.popleft()
                if gene == endGene:
                    return res
                for i in range(8):
                    pattern = gene[:i] + '*' + gene[i + 1:]
                    for nei in geneMap[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            res += 1
        return -1

