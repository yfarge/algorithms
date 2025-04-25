export default function isStringAnagram(str1: string, str2: string): boolean {
    const freq = Array(26).fill(0);

    for (const char of str1) {
        freq[char.charCodeAt(0) - 'a'.charCodeAt(0)] += 1;
    }

    for (const char of str2) {
        if (--freq[char.charCodeAt(0) - 'a'.charCodeAt(0)] < 0) {
            return false;
        }
    }

    return true;
}
