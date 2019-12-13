# Dec 9 2019

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        d_logs = []
        l_logs = []
        for log in logs:
            tmp = log.split()
            if tmp[1].isdigit():
                d_logs.append(log)
            else:
                l_logs.append(log)
        # key function sorts letter logs + identifier in case of ties
        return sorted(l_logs, key=lambda x: x[x.index(' '):] + x[:x.index(' ')]) + d_logs