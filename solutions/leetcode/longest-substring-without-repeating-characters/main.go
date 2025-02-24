package main

func lengthOfLongestSubstring(s string) int {
	seen := make(map[rune]int)
	left, res := 0, 0
	for right, char := range s {
		if lastSeen, ok := seen[char]; ok && lastSeen >= left {
			left = lastSeen + 1
		}
		seen[char] = right
		if right-left+1 > res {
			res = right - left + 1
		}
	}

	return res
}
