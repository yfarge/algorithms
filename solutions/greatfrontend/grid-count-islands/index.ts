export default function countGridIslands(grid: number[][]): number {
    const NUM_ROWS = grid.length;
    const NUM_COLS = grid[0].length;

    function dfs(row: number, col: number): void {
        const stack: [number, number][] = [[row, col]];
        grid[row][col] == 0;

        while (stack.length > 0) {
            const [currentRow, currentCol] = stack.pop() || [];
            if (currentRow == null || currentCol == null) continue;

            for (const [nextRow, nextCol] of [
                [currentRow + 1, currentCol],
                [currentRow, currentCol + 1],
                [currentRow, currentCol - 1],
                [currentRow - 1, currentCol],
            ]) {
                if (nextRow >= 0 && nextRow < NUM_ROWS && currentCol >= 0 && currentCol < NUM_COLS && grid[nextRow][nextCol] == 1) {
                    grid[nextRow][nextCol] = 0;
                    stack.push([nextRow, nextCol]);
                }
            }
        }
    }


    let count = 0;
    for (let i = 0; i < NUM_ROWS; ++i) {
        for (let j = 0; j < NUM_COLS; ++j) {
            if (grid[i][j] == 1) {
                count++;
                dfs(i, j)
            }
        }
    }
    return count;
}
