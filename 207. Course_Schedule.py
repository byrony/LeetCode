# Dec 20 2019

## Topological Sort via DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list        
        adj = [[] for i in range(numCourses)]
        for pre in prerequisites:
            adj[pre[0]].append(pre[1])

        # status: visited 2, visiting 1, unknown 0
        status = [0] * numCourses
        for c in range(numCourses):
            if self.dfs(adj, c, status):
                return False
        return True
    
    def dfs(self, adj, c, status):
        # If it's in visiting, there is cycle
        if status[c] == 1:
            return True
        # If it was visited, no need visit again
        if status[c] == 2:
            return False
        status[c] = 1
        for nei in adj[c]:
            if self.dfs(adj, nei, status):
                return True
        status[c] = 2
        return False


## DFS check check in each path, exceeded time limit
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # create adjacency list
        adj = [None] * numCourses
        for pre in prerequisites:
            if adj[pre[0]] is None:
                adj[pre[0]] = [pre[1]]
            else:
                adj[pre[0]].append(pre[1])
        
        # check if cycle exists
        for course in range(numCourses):
            seen = set([course])
            res = []
            self.hasCycle(adj, course, seen, res)
            if res:
                return res[0]
        return True
    
    def hasCycle(self, adj, course, seen, res):
        if not adj[course]:
            return
        for nei in adj[course]:
            if nei not in seen:
                seen_copy = seen.copy()
                seen_copy.add(nei)
                tmp = self.hasCycle(adj, nei, seen_copy, res)
                if tmp == False:
                    res.append(tmp)
                    return
            else:
                res.append(False)
                return