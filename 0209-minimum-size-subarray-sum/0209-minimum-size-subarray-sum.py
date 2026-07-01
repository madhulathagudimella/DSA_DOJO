class Solution:
    def minSubArrayLen(self,target,nums):
        l=0
        s=0
        ans=len(nums)+1
        for r in range(len(nums)):
            s+=nums[r]
            while s>=target:
                if r-l+1<ans:
                    ans=r-l+1
                s-=nums[l]
                l+=1
        if ans==len(nums)+1:
            return 0
        return ans
