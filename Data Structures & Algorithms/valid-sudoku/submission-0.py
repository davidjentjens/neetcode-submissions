class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        duplicate_grid = defaultdict(set)

        for i in range(n):
            for j in range(n):
                if board[i][j] == ".":
                    continue

                if board[i][j] in duplicate_grid[f'r-{i}']:
                    return False
                else:
                    duplicate_grid[f'r-{i}'].add(board[i][j])

                if board[i][j] in duplicate_grid[f'c-{j}']:
                    return False
                else:
                    duplicate_grid[f'c-{j}'].add(board[i][j])

                i_quadrant, j_quadrant = i // 3, j // 3
                if board[i][j] in duplicate_grid[(i_quadrant, j_quadrant)]:
                    return False
                else:
                    duplicate_grid[(i_quadrant, j_quadrant)].add(board[i][j])

        return True