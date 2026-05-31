class Solution:
    def spiralOrder(self, matrix):
        ans = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while left <= right and top <= bottom:

            # l to  r
            for i in range(left, right + 1):
                ans.append(matrix[top][i])
            top += 1

            # t to  b
            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])
            right -= 1

            # r to  l
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1

            # b to t
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1

        return ans