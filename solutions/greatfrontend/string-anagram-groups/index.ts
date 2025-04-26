export default function anagramGroups(strs: string[]): string[][] {
    const groups: Map<string, string[]> = new Map();
    for (const s of strs) {
        const key = generateFrequency(s);
        if (!groups.has(key)) {
            groups.set(key, []);
        }
        groups.get(key)!.push(s);
    }

    return Array.from(groups.values())
}

function generateFrequency(str: string): string {
    const freq = Array(26).fill(0);
    for (const char of str) {
        freq[char.charCodeAt(0) - 'a'.charCodeAt(0)]++;
    }
    return freq.join("#");
}
