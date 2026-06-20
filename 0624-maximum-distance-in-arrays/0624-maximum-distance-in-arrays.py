class Solution(object):
    def maxDistance(self, arrays):
        mn=arrays[0][0]
        mx=arrays[0][-1]
        ans=0
        for i in range(1,len(arrays)):
            ans=max(ans,abs(arrays[i][-1]-mn),abs(mx-arrays[i][0]))
            mn=min(mn,arrays[i][0])
            mx=max(mx,arrays[i][-1])
        return ans
        