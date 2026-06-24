class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # 横の数
        m = len(matrix[0])
        # 縦の数
        n = len(matrix)


        # 一列の配列にした時のleftとright
        left = 0
        right = (m * n) - 1



        #while loop
        while left <= right:
            # midをmatlixの位置で見つける
            mid = (left + right) // 2
            row = mid // m
            col = mid % m

            print(matrix[row][col])

        # targetがmidと= > <
            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                left = mid + 1
            else:
                right = mid - 1
            
        return False



