package main

func twoSum(nums []int, target int) []int {
	hashmap := make(map[int]int)

	for index, num := range nums {
		complement := target - num
		complementIndex, ok := hashmap[complement]
		if ok {
			return []int{complementIndex, index}
		}
		hashmap[num] = index
	}

	return []int{-1, -1}
}
