class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_height, board_width = len(board), len(board[0])

        # Helper function to get all valid neighbors for a given position
        def get_valid_neighbors(position):
            i, j = position
            valid_neighbors = []
            for pos in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= pos[0] < board_height and 0 <= pos[1] < board_width:
                    valid_neighbors.append(pos)
            return valid_neighbors

        def dfs(start_position, current_word):
            # If the current_word matches the target word, we return True
            if current_word == word:
                return True

            # We must mark the starting letter with a '*', so not to visit it again
            original_letter = board[start_position[0]][start_position[1]]
            board[start_position[0]][start_position[1]] = '*'

            # For every valid neighbor of the start_position letter, we must continue to try
            # to form a word with them
            for (i, j) in get_valid_neighbors(start_position):
                letter = board[i][j]
                # If we reached a '*' character or the current forming word is no longer
                # valid, i.e. not longer a substring of the target word, we can skip this path
                if letter == '*' or current_word + letter not in word:
                    continue
                # Otherwise, we must continue down the line to see if a path can be formed
                if dfs((i,j), current_word + letter):
                    return True

            # After having gone through the possible paths for that letter, we reset its
            # value to the original letter that was there, as not to impact future runs
            board[start_position[0]][start_position[1]] = original_letter
            
            return False
        
        # For every letter, we must attempt to form the word with its subsequent neighbors
        for i in range(board_height):
            for j in range(board_width):
                if dfs((i,j), board[i][j]):
                    return True
        return False
            