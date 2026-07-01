class Solution:
    def characterReplacement(self,s,k):
        d={}
        l=0
        m=0
        ans=0
        for r in range(len(s)):
            d[s[r]]=d.get(s[r],0)+1
            if d[s[r]]>m:
                m=d[s[r]]
            while r-l+1-m>k:
                d[s[l]]-=1
                l+=1
            if r-l+1>ans:
                ans=r-l+1
        return ans