export default function graphIsTree(
    num: number,
    edges: Array<[number, number]>,
): boolean {
    const adj: Record<number, number[]> = {};
    for (let i = 0; i < num; ++i) adj[i] = [];
    for (const [a, b] of edges) {
        adj[a].push(b);
        adj[b].push(a);
    }

    const stack = [0];
    const visited: Set<number> = new Set();
    const recStack: Set<number> = new Set();
    visited.add(0);
    recStack.add(0);

    while (stack.length > 0) {
        const currentNode = stack.pop();
        if (currentNode == null) continue;
        recStack.delete(currentNode);

        for (const neighbor of adj[currentNode]) {
            if (stack.includes(neighbor)) {
                return false;
            }

            if (!visited.has(neighbor)) {
                stack.push(neighbor);
                visited.add(neighbor);
                recStack.add(neighbor);
            }
        }
    }

    return visited.size == num;
}
