function reverseVowels(s: string): string {
    let left = 0, right = s.length - 1;
    const vowels = new Set([
        'a', 'e', 'i', 'o', 'u',
        'A', 'E', 'I', 'O', 'U'
    ]);

    const result = [...s];
    while (left < right) {
        if (!vowels.has(s[left])) {
            left++; continue;
        }

        if (!vowels.has(s[right])) {
            right--; continue;
        }

        [result[left], result[right]] = [result[right], result[left]];
        left++; right--;
    }

    return result.join("");
};
