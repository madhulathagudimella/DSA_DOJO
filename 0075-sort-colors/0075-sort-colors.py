class Solution(object):
    def sortColors(self, nums):
        l,i,e=0,0,len(nums)-1
        while i<=e:
            if nums[i]==0:
                nums[l],nums[i]=nums[i],nums[l]
                l += 1; i += 1
            elif nums[i]==2:
                nums[i],nums[e]=nums[e],nums[i]
                e-=1
            else:
                i+=1
        