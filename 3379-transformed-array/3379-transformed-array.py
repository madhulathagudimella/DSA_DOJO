class Solution:
    def constructTransformedArray(self, nums):
        n=len(nums)
        ans=[]
        for i in range(n):
            idx=(i+nums[i])%n
            ans.append(nums[idx])
        return ans