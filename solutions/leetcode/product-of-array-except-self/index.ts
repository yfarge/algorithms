function productExceptSelf(nums: number[]): number[] {
    const result: number[] = new Array(nums.length);
    result[0] = 1;

    for (let i = 1; i < result.length; i++) {
        result[i] = result[i - 1] * nums[i - 1];
    }

    let right = 1;
    for (let i = result.length - 1; i >= 0; i--) {
        result[i] *= right;
        right *= nums[i];

    }

    return result;
}
