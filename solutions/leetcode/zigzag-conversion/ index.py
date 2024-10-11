class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        current_row = 0
        offset = 1

        for char in s:
            rows[current_row].append(char)
            current_row += offset
            if current_row == 0 or current_row == numRows - 1:
                offset = -offset

        return "".join(["".join(row) for row in rows])
