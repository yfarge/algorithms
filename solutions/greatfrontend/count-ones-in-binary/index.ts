export default function countOnesInBinary(num: number): number {
    let result = 0;
    while (num > 0) {
        result += num & 1;
        num >>>= 1;
    }
    return result;
}
