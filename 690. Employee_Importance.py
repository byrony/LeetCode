# Jan 7 2020

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""

# BFS
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = dict()
        for e in employees:
            dic[e.id] = e 
        
        value = dic[id].importance
        sub = dic[id].subordinates
        while sub:
            next_sub = []
            for s in sub:
                value += dic[s].importance
                next_sub += dic[s].subordinates
            sub = next_sub
        return value


# DFS
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        dic = dict()
        for e in employees:
            dic[e.id] = e 
        value = []
        self.dfs(dic[id], value, dic)
        return sum(value)
        
    def dfs(self, e, value, dic):
        value.append(e.importance)
        for s in e.subordinates:
            self.dfs(dic[s], value, dic)