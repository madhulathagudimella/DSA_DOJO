class Solution:
    def maxSubArray(self, nums):
        curr = 0
        maxi = nums[0]

        for n in nums:
            curr += n
            maxi = max(maxi, curr)

            if curr < 0:
                curr = 0

        return maxi
        