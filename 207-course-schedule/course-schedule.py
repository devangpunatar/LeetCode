class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        visiting = set()

        def dfs(crs):
            if crs in visiting: # cycle detected
                return False
            if crs in visited: # already processed
                return True
            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            visited.add(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
