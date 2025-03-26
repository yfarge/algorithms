export default function maxProductSubArray(numbers: number[]): number {
    let currentMax = numbers[0];
    let currentMin = numbers[0];
    let result = numbers[0];

    for (let i = 1; i < numbers.length; ++i) {
        let tmpMax = currentMax;
        currentMax = Math.max(
            currentMax * numbers[i],
            currentMin * numbers[i],
            numbers[i],
        );
        currentMin = Math.min(
            tmpMax * numbers[i],
            currentMin * numbers[i],
            numbers[i],
        );
        result = Math.max(result, currentMax);
    }

    return result;
}
