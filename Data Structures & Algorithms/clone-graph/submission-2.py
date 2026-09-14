"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        vis = {}

        #returns the node, with its neighbours
        def dfs(node):
            #base case
            if node in vis:
                return vis[node]

            #creates copy, associates with vis
            copy = Node(node.val)
            vis[node] = copy

            #makes copy point to correct neighbours
            for n in node.neighbors:
                vis[node].neighbors.append(dfs(n))

            return vis[node]

        return dfs(node) if node != None else None 
