class Solution(object):
    def subarraySum(self, nums, k):
        d={0:1}
        s=0
        count=0
        for n in nums:
            s+=n
            if s-k in d:
                count+=d[s-k]
            if s in d:
                d[s]+=1
            else:
                d[s]=1
        return count        
        