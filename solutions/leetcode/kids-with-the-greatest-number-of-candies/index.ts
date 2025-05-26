function kidsWithCandies(candies: number[], extraCandies: number): boolean[] {
    const currentMax = Math.max(...candies);
    return candies.map((count) => count + extraCandies >= currentMax);
};
