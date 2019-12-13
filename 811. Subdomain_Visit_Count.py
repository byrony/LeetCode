# Dec 11 2019

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = dict()
        for domain in cpdomains:
            cnt, d = domain.split(' ')
            d_all = d.split('.')
            
            # save all domains into dict
            for i in range(len(d_all)):
                key = '.'.join(d_all[i:])
                if key in dic.keys():
                    dic[key] += int(cnt)
                else:
                    dic[key] = int(cnt)
        
        res = []
        for k, v in dic.items():
            res.append(str(v) + ' ' + str(k))
        return res