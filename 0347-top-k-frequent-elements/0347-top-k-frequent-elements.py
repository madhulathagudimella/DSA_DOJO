class Solution:
    def topKFrequent(self,nums,k):
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        b=[[] for _ in range(len(nums)+1)]
        for n,f in d.items():
            b[f].append(n)
        ans=[]
        for i in range(len(b)-1,0,-1):
            for j in b[i]:
                ans.append(j)
                if len(ans)==k:
                    return ans