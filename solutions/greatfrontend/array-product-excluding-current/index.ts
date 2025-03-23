export default function arrayProductExcludingCurrent(
    numbers: number[],
): number[] {
    const result = Array(numbers.length).fill(0);
    result[0] = 1;

    for (let i = 1; i < numbers.length; ++i) {
        result[i] = result[i - 1] * numbers[i - 1];
    }

    let suffix = 1;
    for (let i = numbers.length - 1; i >= 0; --i) {
        result[i] *= suffix;
        suffix *= numbers[i];
    }

    return result;
}
