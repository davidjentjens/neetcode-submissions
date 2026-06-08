class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_height, board_width = len(board), len(board[0])

        def get_valid_neighbors(start_position):
            i, j = start_position
            valid_neighbors = []
            for pos in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= pos[0] < board_height and 0 <= pos[1] < board_width:
                    valid_neighbors.append(pos)
            return valid_neighbors

        def dfs(start_position, path, current_word):
            nonlocal word
            # If the current_word matches the target word, we return True
            if current_word == word:
                return True
            # For every valid neighbor of the start_position, we must continue to try
            # to form a word with them
            original_letter = board[start_position[0]][start_position[1]]
            board[start_position[0]][start_position[1]] = '*'
            for (i, j) in get_valid_neighbors(start_position):
                letter = board[i][j]
                if letter == '*' or current_word + letter not in word:
                    continue
                board[i][j] = '*'
                if dfs((i,j), path, current_word + letter):
                    return True
                board[i][j] = letter
            board[start_position[0]][start_position[1]] = original_letter
            return False
        
        for i in range(board_height):
            for j in range(board_width):
                if dfs((i,j), [], board[i][j]):
                    return True
        return False
            