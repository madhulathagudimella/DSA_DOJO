class Solution:
    def findMaxAverage(self,nums,k):
        s=0
        for i in range(k):
            s+=nums[i]
        ans=s
        for i in range(k,len(nums)):
            s+=nums[i]
            s-=nums[i-k]
            if s>ans:
                ans=s
        return ans/float(k)