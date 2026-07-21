class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # If the number of edges exceeds n-1, 
        # it definitely cannot be a tree. 
        # (a tree with n vertices has exactly n-1 edges; 
        # one more edge would form a cycle).
        if len(edges) > (n - 1):
            return False
        
        adj = [[]for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            visit.add(node)
            for nei in adj[node]:
                if nei == par:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visit) == n
