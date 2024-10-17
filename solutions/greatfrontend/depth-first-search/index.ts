export default function depthFirstSearch(
  graph: Record<string, Array<string>>,
  source: string,
): Array<string> {
  if (Object.keys(graph).length === 0) {
    return [];
  }

  const stack: Array<string> = [source];
  const visited = new Set<string>();

  while (stack.length) {
    const node = stack.pop()!;
    visited.add(node);

    const neighbors = graph[node];
    for (let i = neighbors.length - 1; i >= 0; i--) {
      const neighbor = neighbors[i];
      if (!visited.has(neighbor)) {
        stack.push(neighbor);
      }
    }
  }
  return Array.from(visited);
}
