class Solution:
    def letterCombinations(self,digits):
        if len(digits)==0:
            return []
        data={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result=[]
        def find(index,word):
            if index==len(digits):
                result.append(word)
                return
            for letter in data[digits[index]]:
                find(index+1,word+letter)
        find(0,"")
        return result