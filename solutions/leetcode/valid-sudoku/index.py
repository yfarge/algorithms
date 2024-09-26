class Solution(object):
    def containsDuplicates(self, l):
        l = list(filter(lambda x: x != '.', l))
        return len(l) != len(set(l))

    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # Check row duplicates
        for j in range(9):
            if self.containsDuplicates(board[j]):
                return False

        # Check column duplicates
        for j in range(9):
            column = [row[j] for row in board]
            if self.containsDuplicates(column):
                return False

        # Check 3x3 sub-boxes
        seen = set()
        box_starts = [(i, j) for i in range(0, 9, 3) for j in range(0, 9, 3)]
        for x_start, y_start in box_starts:
            for column in range(9):
                cell = board[x_start + column % 3][y_start + column // 3]
                if cell != "." and cell in seen:
                    return False
                seen.add(cell)
            seen.clear()
        return True
