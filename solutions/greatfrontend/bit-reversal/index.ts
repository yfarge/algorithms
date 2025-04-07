export default function bitReversal(n: number): number {
    let result = 0;
    for (let i = 31; i >= 0; --i) {
        result |= (n & 1) << i;
        n >>>= 1;
    }

    return result >>> 0;
}
