export default function graphCountConnectedComponents(
  n: number,
  edges: Array<[number, number]>,
): number {

  function dfs(node: number): void {
    const stack: number[] = [node];
    visited.add(node);

    while (stack.length > 0) {
      const currentNode = stack.pop();
      if (currentNode == null) continue;

      for (const neighbor of adj[currentNode]) {
        if (!visited.has(neighbor)) {
          stack.push(neighbor);
        }
        visited.add(neighbor);
      }
    }
  }

  const adj: Record<number, number[]> = {};
  for (let i = 0; i < n; ++i) {
    adj[i] = [];
  }

  for (const [a, b] of edges) {
    adj[a].push(b);
    adj[b].push(a);
  }

  let count = 0;
  const visited: Set<number> = new Set();
  for (let i = 0; i < n; ++i) {
    if (!visited.has(i)) {
      count++;
      dfs(i);
    }
  }

  return count;
}
