# Jan 12 2020

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # create adjacency list
        adj = [[] for _ in range(numCourses)]
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])
        
        # course status: 1-visting, 2-visited, 0-unknown
        res = []
        status = [0]*numCourses
        for n in range(numCourses):
            curr = []
            # if cycle exists, return [] 
            if self.dfs(adj, n, status, curr):
                return []
            else:
                res += curr
        return res
            
    def dfs(self, adj, n, status, curr):
        # if visited before, return False
        if status[n] == 2:
            return False
        # if is visiting, return True, means cycle exists
        if status[n] == 1:
            return True
        status[n] = 1
        for pre in adj[n]:
            if self.dfs(adj, pre, status, curr):
                return True
        status[n] = 2
        curr.append(n)
        return False