class Solution:
    def solve(self, board: List[List[str]]) -> None:
        board_height, board_width = len(board), len(board[0])

        def isInBoard(pos):
            r, c = pos
            return 0 <= r < board_height and 0 <= c < board_width

        def isBorder(pos):
            if not isInBoard(pos):
                return False
            r, c = pos
            return r == 0 or c == 0 or r == board_height-1 or c == board_width-1

        def getValidNeighbors(start_pos):
            r, c = start_pos
            valid_neighbors = []
            for pos in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if isInBoard(pos) and board[pos[0]][pos[1]] == 'O':
                    valid_neighbors.append(pos)
            return valid_neighbors

        queue = deque()
        visited = set()
        for r in range(board_height):
            for c in range(board_width):
                if board[r][c] == 'O' and isBorder((r,c)):
                    queue.append((r,c))
                    visited.add((r,c))

        while queue:
            pos = queue.popleft()
            board[pos[0]][pos[1]] = '-'
            for neighbor in getValidNeighbors(pos):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        for r in range(board_height):
            for c in range(board_width):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '-':
                    board[r][c] = 'O'                