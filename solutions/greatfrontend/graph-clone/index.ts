interface GraphNode {
    val: number;
    neighbors: GraphNode[];
}

export default function graphClone(node: GraphNode | null): GraphNode | null {
    if (node == null) {
        return null
    }

    const nodes: Map<number, GraphNode> = new Map();
    function dfs(node: GraphNode) {
        if (nodes.has(node.val)) {
            return nodes.get(node.val)!;
        }

        const copiedNode: GraphNode = { val: node.val, neighbors: [] };
        nodes.set(node.val, copiedNode)

        for (const neighbor of node.neighbors) {
            copiedNode.neighbors.push(dfs(neighbor))
        }

        return copiedNode;
    }

    return dfs(node);
}
