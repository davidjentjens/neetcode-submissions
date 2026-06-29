class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        min_row, max_row = 0, len(matrix)-1
        while min_row <= max_row:
            target_row = (min_row + max_row) // 2
            if target > matrix[target_row][-1]:
                min_row = target_row + 1
            elif target < matrix[target_row][0]:
                max_row = target_row - 1
            else:
                break

        min_pos, max_pos = 0, len(matrix[0])-1
        print(matrix[target_row])
        while min_pos <= max_pos:
            mid_pos = (min_pos + max_pos) // 2
            print(matrix[target_row][min_pos], matrix[target_row][mid_pos], matrix[target_row][max_pos])

            if matrix[target_row][mid_pos] == target:
                return True

            if target > matrix[target_row][mid_pos]:
                min_pos = mid_pos + 1
            else:
                max_pos = mid_pos - 1

        return False