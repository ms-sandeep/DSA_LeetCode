class Solution(object):
    def searchMatrix(self, matrix, target):
        rows = len(matrix)
        cols = len(matrix[0])

        low = 0
        high = rows * cols - 1

        while low <= high:
            mid = (low + high) // 2

            r = mid // cols
            c = mid % cols

            middle_value = matrix[r][c]

            if middle_value == target:
                return True

            elif middle_value < target:
                low = mid + 1

            else:
                high = mid - 1

        return False