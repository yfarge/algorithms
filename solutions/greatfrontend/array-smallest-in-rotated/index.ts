export default function smallestInRotatedArray(numbers: number[]): number {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        let mid = Math.trunc((left + right) / 2);

        if (numbers[mid] <= numbers[right]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return numbers[right];
}
