class TrieNode {
    public isTerminal: boolean;
    public children: Map<string, TrieNode>

    constructor() {
        this.isTerminal = false;
        this.children = new Map();
    }
}

export default class Trie {
    private root = new TrieNode();

    public insert(word: string): void {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char)!;
        }
        node.isTerminal = true;
    }

    public search(word: string): boolean {
        let node = this.root;
        for (const char of word) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char)!
        }
        return node.isTerminal;
    }

    public startsWith(prefix: string): boolean {
        let node = this.root;
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char)!
        }
        return true;
    }
}

