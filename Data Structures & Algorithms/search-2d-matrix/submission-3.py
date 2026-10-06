class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW = len(matrix)
        COL = len(matrix[0])
        
        top = 0
        bottom = ROW - 1

        l = 0
        r = COL - 1

        while top <= bottom:
            m = (bottom + top) // 2

            if target < matrix[m][0]:
                bottom = m - 1
            elif target > matrix[m][-1]:
                top = m + 1
            else:
                while l <= r:
                    m2 = (r + l) // 2

                    if target > matrix[m][m2]:
                        l = m2 + 1
                    
                    elif target < matrix[m][m2]:
                        r = m2 -1

                    else:
                        return True

                return False
                
        
        return False


        