export default function findWordInGrid(
    grid: string[][],
    target: string,
): boolean {
    const m = grid.length;
    const n = grid[0].length;

    function backtrack(row: number, col: number, wordIndex: number): boolean {
        if (wordIndex === target.length) {
            return true;
        }

        if (
            row < 0 || m <= row ||
            col < 0 || n <= col ||
            grid[row][col] != target[wordIndex]
        ) {
            return false;
        }

        grid[row][col] = "#";

        const result = (
            backtrack(row, col - 1, wordIndex + 1) ||
            backtrack(row - 1, col, wordIndex + 1) ||
            backtrack(row, col + 1, wordIndex + 1) ||
            backtrack(row + 1, col, wordIndex + 1)
        );

        grid[row][col] = target[wordIndex];

        return result;
    }

    for (let i = 0; i < m; ++i) {
        for (let j = 0; j < n; ++j) {
            if (backtrack(i, j, 0)) {
                return true;
            }
        }
    }

    return false;
}
