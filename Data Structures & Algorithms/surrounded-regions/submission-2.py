from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        board_height, board_width = len(board), len(board[0])

        def isBorder(pos):
            r, c = pos
            return r == 0 or r == board_height-1 or c == 0 or c == board_width-1

        def getValidNeighbors(start_pos):
            r, c = start_pos
            valid_neighbors = []
            for pos in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                if 0 <= pos[0] < board_height and 0 <= pos[1] < board_width and board[pos[0]][pos[1]] == 'O':
                    valid_neighbors.append(pos)
            return valid_neighbors

        queue = deque()

        for i in range(board_height):
            for j in range(board_width):
                if isBorder((i,j)) and board[i][j] == 'O':
                    queue.append((i,j))

        while queue:
            node = queue.popleft()
            r, c = node
            board[r][c] = 'V'
            for neighbor in getValidNeighbors(node):
                queue.append(neighbor)

        for i in range(board_height):
            for j in range(board_width):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'V':
                    board[i][j] = 'O'
            