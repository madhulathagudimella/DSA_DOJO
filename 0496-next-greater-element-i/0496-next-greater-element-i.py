class Solution:
    def nextGreaterElement(self,nums1,nums2):
        st=[]
        d={}
        for i in nums2:
            while st and i>st[-1]:
                d[st.pop()]=i
            st.append(i)
        while st:
            d[st.pop()]=-1
        return[d[i]for i in nums1]