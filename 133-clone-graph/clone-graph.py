"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        def dfs(node):
            if not node:
                return None
            
            if node in hashMap:
                return hashMap[node]

            # Clone the node
            clone = Node(node.val)
            hashMap[node] = clone

            # Recursively clone neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)